import re
import os
import sys
import json
import subprocess
import ipaddress

def leer_archivo(data_path):
    try:
        with open(data_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(json.dumps({'error': f"Error al leer el archivo: {e}"}))
        return None

def buscar_primera_coincidencia(patrones, texto):
    for patron in patrones:
        resultado = re.search(patron, texto)
        if resultado:
            return resultado.group(1).strip()
    return "No encontrado"

def ejecutar_enlace(cfs):
    url = f"http://dkvapi.lat.intranet/gpin.html?CFSID={cfs}&ActCountry=MEX&ActUCase=PRO&DVReadOnly=0"
    subprocess.Popen(['wslview', url])

def main(cfs):
    data_path = os.path.join('data', f'{cfs}.txt')

    if not os.path.exists(data_path):
        print(json.dumps({'error': f"El archivo {data_path} no existe."}))
        return

    texto = leer_archivo(data_path)
    if texto is None:
        return

    patrones_busqueda = {
        'pe': [ r'PTO\s*([^\s,]+)', r'PE:\s*([^\s,]+)',],
        'asn': [r'AS_BGP:\s*(\d+)', r'ASN:\s*(\d+)'],
        'bw': [r'@(\d+[MG]b)', r'(\d+)[MG]b', r'BW:\s*(\d+)[MG]'],
        'cfs': [r'CID-CFS :\s*(\d+)', r'CFS-CID:\s*(\d+)', r'CID-CFS:\s*(\d+)', r'CFS:\s*(\d+)', r'CFS\s*(\d+)'],
        'cliente': [r'(?i)CLIENTE:\s*(.*?)(?=\n)', r'(?i)Cliente:\s*(.*?)(?=\n)', r'(?i)CLIENT:\s*(.*?)(?=\n)'],
        'configuracion': [r'(Alta)', r'(ampliación)'],
        'cvlan': [r'Cvlan:\s*(\d+)'],
        'dko': [r'DKO:\s*(\d+)'],
        'interface_pe': [r'Interface PE:\s*([^\s,]+)', r'PTO\s*[^\s,]+\s*([^\s,]+)'],
        'interface_sw': [r'DEVICE:\s*[^\s,]+\s+(Te\d+/\d+/\d+/\d+)', r'Interface SW:\s*([^\s,]+)', r'INTERCONEXION\s*-\s*[^\s,]+\s*-\s*PTO\s*(TENGIGA\s*\d+/\d+/\d+/\d+)'],
        'lnnid': [r'LB NID:\s*([\d.]+)'],
        'pais': [r'(MEXICO)'],
        'rd': [r'RD:\s*([^\s,]+)'],
        'rfs_ip_port': [r'RFS IP PORT:\s*(\d+)', r'RFS IP Port:\s*(\d+)', r'IP Port :\s*(\d+)', r'(\d+)\s*IP Port\s*', r'\*:\s*RFS(\d+)\s*\( IP Port \)', r'\*:\s*(\d+)\s*\(IP Port\)', r'\*:\s*RFS\s*(\d+)\s*\( IP Port \)'],
        'rfs_ip_port_nid': [r'NID\s*:\s*(\d+)', r'\*:\s*RFS\s*(\d+)\s*\(\s*NID\s*\)', r'\*:\s*RFS\s*(\d+)\s*\( NID \)'],
        'sede': [r'(?i)Sede\s*:\s*(.*)', r'(?i)SITE:\s*(.*)'],
        'svlan': [r'Svlan:\s*(\d+)'],
        'sw': [r'DEVICE:\s*([^\s,]+)', r'SW:\s*([^\s,]+)', r'ME:\s*([^\s,]+)', r'DEVICE:\s*([^\s]+)', r'INTERCONEXION\s*-\s*([^\s,]+)'],
        'tipo': [r'(Internet)', r'(VPN)'],
        'vlan': [r'VLAN\s*(\d+)', r'S-VLAN:\s*(\d+)', r'VLAN ASIGNADA:\s*(\d+)'],
        'vrf': [r'VRF:\s*(.*)'],
        'wan': [r'IP_WAN:\s*([\d./]+)', r'WAN:\s*([\d./]+)'],
        'wanv6': [r'WANIPv6:\s*([\da-fA-F:]+/\d+)'],
        'lbcpe': [r'CPE :\s*([\d.]+)', r'LB CPE:\s*([\d.]+)']        

    }

    resultados = {clave: buscar_primera_coincidencia(patrones, texto) for clave, patrones in patrones_busqueda.items()}

    if resultados['wan'] != "No encontrado":
        try:
            ip_network = ipaddress.ip_network(resultados['wan'], strict=False)
            resultados['wan'] = str(ip_network.network_address) + '/' + str(ip_network.prefixlen)
        except ValueError as e:
            resultados['wan'] = f"Error al convertir IP: {e}"
    else:
        resultados['wan'] = "0.0.0.0/0"

    if resultados['wanv6'] != "No encontrado":
        try:
            ip_network_v6 = ipaddress.ip_network(resultados['wanv6'], strict=False)
            resultados['wanv6'] = str(ip_network_v6.network_address) + '/' + str(ip_network_v6.prefixlen)
        except ValueError as e:
            resultados['wanv6'] = f"Error al convertir IP: {e}"
    else:
        resultados['wanv6'] = "::/0"


    if resultados['bw'] != "No encontrado":
        if "1Gbps" in texto:
            resultados['bw'] = "1000"
        else:
            match = re.match(r'(\d+)([MG]b)', resultados['bw'])
            if match:
                bw_valor, unidad = match.groups()
                bw_valor = int(bw_valor)
                if unidad == "Gb":
                    bw_valor *= 1000
                resultados['bw'] = f"{bw_valor}"

    tipo_servicio = "ADI" if resultados['tipo'] == "Internet" else "VPN" if resultados['tipo'] == "VPN" else "No encontrado"


    # Asignar "Juniper" a tipo_equipo si se encuentra "MEXICO" y tipo_servicio es "ADI"
    tipo_equipo = "JUNIPER" if (resultados['pais'] != "No encontrado" and tipo_servicio == "ADI") or ("edge" in resultados['pe'].lower()) else "No encontrado"

    # Buscar la palabra "VPN" en el texto y asignar "VPN" a la variable vpn si se encuentra
    vpn = "VPN" if "VPN" in texto else "No encontrado"
    # Si se encuentra "VPN", asignar "Juniper" a tipo_equipo
    if vpn == "VPN":
        tipo_equipo = "JUNIPER"

    # Asignar "Alta" a tipo_configuracion si se encuentra "Alta"
    tipo_configuracion = "Alta" if resultados['configuracion'] == "Alta" else "Ampliacion" if resultados['configuracion'] == "ampliación" else "No encontrado"

    # Eliminar valores comunes entre "cliente" y "sede" manteniendo el orden
    if resultados['cliente'] != "No encontrado" and resultados['sede'] != "No encontrado":
        cliente_palabras = resultados['cliente'].split()
        sede_palabras = resultados['sede'].split()
        valores_unicos_sede = [palabra for palabra in sede_palabras if palabra not in cliente_palabras]
        resultados['sede'] = ' '.join(valores_unicos_sede) if valores_unicos_sede else "No encontrado"

    # Limpiar espacios y guiones al inicio de "sede"
    if resultados['sede'] != "No encontrado":
        resultados['sede'] = resultados['sede'].lstrip(" -")

    # Dejar "asn" en blanco si es "No encontrado"
    if resultados['asn'] == "No encontrado":
        resultados['asn'] = ""

    # Dejar "lbcpe" en blanco si es "No encontrado"
    if resultados['lbcpe'] == "No encontrado":
        resultados['lbcpe'] = ""

    # Dejar "sw" en blanco si es "No encontrado"
    if resultados['sw'] == "No encontrado":
        resultados['sw'] = ""

    # Dejar "vlan" en blanco si es "No encontrado"
    if resultados['vlan'] == "No encontrado":
        resultados['vlan'] = ""

    # Dejar "interface_sw" en blanco si es "No encontrado"
    if resultados['interface_sw'] == "No encontrado":
        resultados['interface_sw'] = ""

    if resultados['lnnid'] == "No encontrado":
        resultados['lnnid'] = ""

    if resultados['pe'] != "No encontrado":
        resultados['sw'] = "Conectado a PE"

    if resultados['asn'] == "No encontrado":
        resultados['asn'] = ""

    if resultados['lbcpe'] == "No encontrado":
        resultados['lbcpe'] = ""

    if resultados['sw'] == "No encontrado":
        resultados['sw'] = ""

    if resultados['vlan'] == "No encontrado":
        resultados['vlan'] = ""

    if resultados['interface_sw'] == "No encontrado":
        resultados['interface_sw'] = ""

    if resultados['lnnid'] == "No encontrado":
        resultados['lnnid'] = ""

    if resultados['svlan'] == "No encontrado":
        resultados['svlan'] = ""

    if resultados['cvlan'] == "No encontrado":
        resultados['cvlan'] = ""

    if any(resultados[clave] == "No encontrado" for clave in ['cliente', 'sede', 'cfs', 'rfs_ip_port', 'rfs_ip_port_nid']):
        ejecutar_enlace(cfs)

    resultados['tipo_servicio'] = tipo_servicio
    resultados['tipo_equipo'] = tipo_equipo
    resultados['tipo_configuracion'] = tipo_configuracion

    print(json.dumps(resultados))

if __name__ == "__main__":
    cfs = sys.argv[1] if len(sys.argv) > 1 else ""
    main(cfs)