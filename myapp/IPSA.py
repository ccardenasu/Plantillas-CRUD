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

def buscar_sw_int(texto):
    patron_sw = r'SW:\s*([^\s,]+)'
    patron_int = r'Int:\s*([^\s,]+)'
    
    # Buscar "SW:"
    match_sw = re.search(patron_sw, texto)
    if match_sw:
        # Buscar "Int:" en la siguiente línea
        lineas = texto.split('\n')
        for i, linea in enumerate(lineas):
            if re.search(patron_sw, linea):
                if i + 1 < len(lineas):
                    match_int = re.search(patron_int, lineas[i + 1])
                    if match_int:
                        return match_int.group(1).strip()
    return "No encontrado"


def main(cfs):
    data_path = os.path.join('data', f'{cfs}.txt')

    if not os.path.exists(data_path):
        print(json.dumps({'error': f"El archivo {data_path} no existe."}))
        return

    texto = leer_archivo(data_path)
    if texto is None:
        return
    
    patrones_busqueda = {
        'sw':  [ r'SW:\s*([^\s,]+)\s*-\s*TEN GIGA\s*[^\s,]+', r'SW:\s*(\d+)', r'DEVICE:\s*([^\s,]+)', r'SW:\s*([^\s,]+)', r'ME:\s*([^\s,]+)', r'DEVICE:\s*([^\s]+)', r'INTERCONEXION\s*-\s*([^\s,]+)', r'NNI\s*[^\s,]+\s*-\s*([^\s,]+)', ],
        'rfs_ip_port_punta_a': [r'RFS IP Port de VPLS - Punta A:\s*(\d+)'],
        'lag': [r'Int:\s*ae-(\d+):\d+\.\d+'],
        'interface_pe': [r'Interface PE:\s*([^\s,]+)', r'PTO\s*[^\s,]+\s*([^\s,]+)', r'Int:\s*(ae-\d+):\d+\.\d+'],
        'svlan': [r'Int:\s*ae-\d+:(\d+)\.\d+', r'Svlan:\s*(\d+)', r'INT:\s*ae\d+\.(\d+)'],
        'cvlan': [ r'Int:\s*ae-\d+:\d+\.(\d+)',r'Cvlan:\s*(\d+)',],
        'bw': [r'\b(\d+)Mbps\b.*', r'\b(\d+)Gb\b.*', r'\b(\d+)Mb\b.*'],
        'pe': [ r'PTO\s*([^\s,]+)',r'(?<!C)PE:\s*([^\s,]+)', r'PE:\s*([^\s,]+)'],
        'voz': [r'Voz\s*(\d+)%'],
        'video': [r'Video\s*(\d+)%'],
        'tipo': [r'(VPN)',r'(Internet)',  r'(EPL)'],
        'be': [r'INT:\s*(ae\d+)\.\d+'],
        'sw': [r'NODO\s*(\d+)', r'SW:\s*([^\s,]+)\s*-\s*TEN GIGA\s*[^\s,]+', r'SW:\s*(\d+)', r'DEVICE:\s*([^\s,]+)', r'SW:\s*([^\s,]+)', r'ME:\s*([^\s,]+)', r'DEVICE:\s*([^\s]+)', r'INTERCONEXION\s*-\s*([^\s,]+)', r'NNI\s*[^\s,]+\s*-\s*([^\s,]+)', ],
        'sede': [r'(?i)Site:\s*(.*)', r'(?i)Sede\s*:\s*(.*)', r'(?i)SITE:\s*(.*)', ],
        'rd': [r'RD:\s*([^\s,]+)'],
        'vrf': [r'VRF:\s*(.*)',r'vrf:\s*(.*)'],
        'rfs_ip_port_nid': [r'NID\s*:\s*(\d+)', r'\*:\s*RFS\s*(\d+)\s*\(\s*NID\s*\)', r'\*:\s*RFS\s*(\d+)\s*\( NID \)',r'RFS NID - Punta Z:\s*(\d+)'],
        'asn': [r'AS_BGP:\s*(\d+)', r'ASN:\s*(\d+)',r'ASN\s*(\d+)'],
        'cfs': [r'CFS :\s*(\d+)',r'CID-CFS :\s*(\d+)', r'CFS-CID:\s*(\d+)', r'CID-CFS:\s*(\d+)', r'CFS:\s*(\d+)',r'CFS ID:\s*(\d+)', r'CFS\s*(\d+)'],
        'cliente': [r'(?i)Customer:\s*(.*?)(?=\n)',r'(?i)CLIENTE:\s*(.*?)(?=\n)', r'(?i)Cliente:\s*(.*?)(?=\n)', r'(?i)CLIENT:\s*(.*?)(?=\n)', ],
        'configuracion': [r'(Alta)', r'(alta)', r'(ampliación)', r'(ampliacion)'],
        'dko': [r'DKO:\s*(\d+)'],
        'interface_sw': [r'(TE\d+/\d+/\d+/\d+)',r'TE\d+/\d+/\d+/\d+',r'DEVICE:\s*[^\s,]+\s+(Te\d+/\d+/\d+/\d+)', r'Interface SW:\s*([^\s,]+)', r'INTERCONEXION\s*-\s*[^\s,]+\s*-\s*PTO\s*(TENGIGA\s*\d+/\d+/\d+/\d+)'],
        'lnnid': [r'LB NID:\s*([\d.]+)'],
        'pais': [r'(MEXICO)'],
        'rd': [r'RD:\s*([^\s,]+)'],
        'rfs_ip_port': [r'IP Port:\s*(\d+)',r'IP PORT:\s*(\d+)', r'RFS IP PORT:\s*(\d+)', r'RFS IP Port:\s*(\d+)', r'IP Port :\s*(\d+)', r'(\d+)\s*IP Port\s*', r'\*:\s*RFS(\d+)\s*\( IP Port \)', r'\*:\s*(\d+)\s*\(IP Port\)', r'\*:\s*RFS\s*(\d+)\s*\( IP Port \)',r'RFS IP Port de VPLS - Punta Z:\s*(\d+)'],
        'sede': [r'(?i)Sede\s*:\s*(.*)', r'(?i)SITE:\s*(.*)', r'(?i)A-Side Site:\s*(.*)'],
        'vlan': [r'vlan\s*(\d+)',r'VLAN\s*(\d+)', r'S-VLAN:\s*(\d+)', r'VLAN ASIGNADA:\s*(\d+)'],
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

     # Validar y convertir el valor de 'bw'
    # Validar y convertir el valor de 'bw'
    if resultados['bw'] != "No encontrado":
        if 'Mb' in resultados['bw']:
            resultados['bw'] = int(re.search(r'\d+', resultados['bw']).group())
        elif 'Mbps' in resultados['bw']:
            resultados['bw'] = int(re.search(r'\d+', resultados['bw']).group())
        elif 'Gb' in resultados['bw']:
            resultados['bw'] = int(re.search(r'\d+', resultados['bw']).group()) * 1000
        elif 'Gbps' in resultados['bw']:
            resultados['bw'] = int(re.search(r'\d+', resultados['bw']).group()) * 1000

    be = "Bundle-ether10" if resultados['be'] == "ae10" else "bundle_ether11" if resultados['tipo'] == "ae11" else "bundle_ether14" if resultados['tipo'] == "ae14" else "No encontrado"

    # Asignar el tipo de servicio basado en el valor de 'tipo'
    tipo_servicio = "ADI" if resultados['tipo'] == "Internet" else "VPN" if resultados['tipo'] == "VPN" else "VPLS" if resultados['tipo'] == "EPL" else "No encontrado"

    # Asignar "Juniper" a tipo_equipo si se encuentra "MEXICO" y tipo_servicio es "ADI"
    # o si "edge" está en 'pe' o si se encuentra la palabra "EPL" en el texto
    tipo_equipo = "ALCATEL" if "ar" in resultados['pe'].lower() else "JUNIPER" if (resultados['pais'] != "No encontrado" and tipo_servicio == "ADI") or ("edge" in resultados['pe'].lower()) or ("EPL" in texto) else "No encontrado"
    
    
    # Buscar la palabra "VPN" en el texto y asignar "VPN" a la variable vpn si se encuentra
    vpn = "VPN" if "VPN" in texto else "No encontrado"
    # Si se encuentra "VPN", asignar "Juniper" a tipo_equipo
    if vpn == "VPN":
        tipo_equipo = "JUNIPER"

    # Asignar "Alta" a tipo_configuracion si se encuentra "Alta"
    if resultados['configuracion'] in ["Alta", "alta"]:
        tipo_configuracion = "Alta"
    elif resultados['configuracion'] in ["ampliación", "ampliacion"]:
        tipo_configuracion = "Ampliacion"
    else:
        tipo_configuracion = "No encontrado"

    # Eliminar valores comunes entre "cliente" y "sede" manteniendo el orden
    if resultados['cliente'] != "No encontrado" and resultados['sede'] != "No encontrado":
        cliente_palabras = resultados['cliente'].split()
        sede_palabras = resultados['sede'].split()
        valores_unicos_sede = [palabra for palabra in sede_palabras if palabra not in cliente_palabras]
        resultados['sede'] = ' '.join(valores_unicos_sede) if valores_unicos_sede else "No encontrado"
   
    if resultados['rfs_ip_port_nid'] == "No encontrado":
        resultados['rfs_ip_port_nid'] = ""
    # Dejar "be" en blanco si es "No encontrado"
    if resultados['be'] == "No encontrado":
        resultados['be'] = ""
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

   # Si 'pe' no es "No encontrado", actualizar 'sw'
    if resultados['pe'] != "No encontrado" and resultados['sw'] == "No encontrado":
        resultados['sw'] = "Conectado a PE"

    # Nueva condición adicional
    if resultados['pe'] == "edge1.bgo2" and resultados['interface_pe'] == "et-0/0/18":
        resultados['interface_pe'] = "ae30"

    if resultados['asn'] == "No encontrado":
        resultados['asn'] = ""

    if resultados['lbcpe'] == "No encontrado":
        resultados['lbcpe'] = ""

    if resultados['sw'] == "No encontrado":
        resultados['sw'] = ""

    if resultados['vlan'] == "No encontrado":
        resultados['vlan'] = ""

    if resultados['lnnid'] == "No encontrado":
        resultados['lnnid'] = ""

    if resultados['svlan'] == "No encontrado":
        resultados['svlan'] = ""

    if resultados['cvlan'] == "No encontrado":
        resultados['cvlan'] = ""

    if resultados['rfs_ip_port_punta_a'] == "No encontrado":
        resultados['rfs_ip_port_punta_a'] = ""

    if resultados['tipo'] == "EPL":
        cliente_modificado = resultados['cliente'].replace(" ", "-")
        resultados['vrf'] = f"{resultados['cfs']}-{cliente_modificado}"
        resultados['rd'] = resultados['cfs']

    if any(resultados[clave] == "No encontrado" for clave in ['cliente', 'sede', 'cfs', 'rfs_ip_port', 'rfs_ip_port_nid']):
        ejecutar_enlace(cfs)

    resultados['tipo_servicio'] = tipo_servicio
    resultados['tipo_equipo'] = tipo_equipo
    resultados['tipo_configuracion'] = tipo_configuracion
    resultados['be'] = be
    resultados['interface_sw'] = buscar_sw_int(texto)



    print(json.dumps(resultados))

if __name__ == "__main__":
    cfs = sys.argv[1] if len(sys.argv) > 1 else ""
    main(cfs)