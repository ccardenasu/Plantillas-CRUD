import re
import os
import sys
import json
import subprocess
import ipaddress
import logging

def leer_archivo(data_path):
    try:
        with open(data_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"El archivo {data_path} no existe.")
    except IOError as e:
        logging.error(f"Error al leer el archivo: {e}")
    return None

def buscar_primera_coincidencia(patrones, texto):
    if not patrones or not texto:
        return "No encontrado"
    for patron in patrones:
        resultado = re.search(patron, texto)
        if resultado:
            return resultado.group(1).strip()
    return "No encontrado"

def ejecutar_enlace(cfs):
    url = f"http://dkvapi.lat.intranet/gpin.html?CFSID={cfs}&ActCountry=MEX&ActUCase=PRO&DVReadOnly=0"
    try:
        subprocess.Popen(['wslview', url])
    except Exception as e:
        logging.error(f"Error al ejecutar el enlace: {e}")

def buscar_sw_int(texto):
    if not texto:
        return "No encontrado"
    
    patron_sw = r'SW:\s*([^\s,]+)'
    patron_int = r'Int:\s*([^\s,]+)'
    
    match_sw = re.search(patron_sw, texto)
    if match_sw:
        lineas = texto.split('\n')
        for i, linea in enumerate(lineas):
            if re.search(patron_sw, linea):
                if i + 1 < len(lineas):
                    match_int = re.search(patron_int, lineas[i + 1])
                    if match_int:
                        return match_int.group(1).strip()
    return "No encontrado"

def buscar_ufinet_nni(texto):
    if not texto:
        return "No encontrado"
    
    patron = r'(.*UFINET.*NNI.*2\.1.*)'
    match = re.search(patron, texto, re.IGNORECASE)
    if match:
        return True
    return False

def buscar_LIBERTY_nni(texto):
    if not texto:
        return "No encontrado"
    
    patron = r'(.*LIBERTY.*NNI.*Bogotá.*)'
    match = re.search(patron, texto, re.IGNORECASE)
    if match:
        return True
    return False



def main(cfs):
    data_path = os.path.join('data', f'{cfs}.txt')

    if not os.path.exists(data_path):
        logging.error(f"El archivo {data_path} no existe.")
        return

    texto = leer_archivo(data_path)
    if texto is None:
        return
    
    patrones_busqueda = {
        'asn': [r'AS_BGP:\s*(\d+)', r'ASN:\s*(\d+)', r'ASN\s*(\d+)'],
        'be': [r'INT:\s*(ae\d+)\.\d+'],
        'bw': [r'\b(\d+)Mbps\b.*', r'\b(\d+)Gb\b.*', r'\b(\d+)Mb\b.*'],
        'bw_exchange': [r'(\d+)% E --'],
        'bw_plus': [r'(\d+)% P --'],
        'cfs': [r'CFS:\s*(\d+)',r'CFS :\s*(\d+)', r'CID-CFS :\s*(\d+)', r'CFS-CID:\s*(\d+)', r'CID-CFS:\s*(\d+)', r'CFS:\s*(\d+)', r'CFS\s+ID:\s*(\d+)', r'CFS\s*(\d+)'],
        'cliente': [r'(?i)Customer:\s*(.*?)(?=\n)', r'(?i)CLIENTE:\s*(.*?)(?=\n)', r'(?i)Cliente:\s*(.*?)(?=\n)', r'(?i)CLIENT:\s*(.*?)(?=\n)'],
        'configuracion': [r'(Alta)', r'(alta)', r'(ampliación)', r'(ampliacion)'],
        'cvlan': [r'Int:\s*ae-\d+:\d+\.(\d+)', r'Cvlan:\s*(\d+)'],
        'dko': [r'DKO:\s*(\d+)'],
        'interface_pe': [r'Interface PE:\s*([^\s,]+)', r'PTO\s*[^\s,]+\s*([^\s,]+)', r'Int:\s*(ae-\d+):\d+\.\d+'],
        'interface_pe_b': [r'CLIENT_b:\s*(.*?)(?=\n)'],
        'interface_sw': [r'(TE\d+/\d+/\d+/\d+)', r'TE\d+/\d+/\d+/\d+', r'DEVICE:\s*[^\s,]+\s+(Te\d+/\d+/\d+/\d+)', r'Interface SW:\s*([^\s,]+)', r'INTERCONEXION\s*-\s*[^\s,]+\s*-\s*PTO\s*(TENGIGA\s*\d+/\d+/\d+/\d+)'],
        'lag': [r'Int:\s*ae-(\d+):\d+\.\d+'],
        'lbcpe': [r'CPE :\s*([\d.]+)', r'LB CPE:\s*([\d.]+)'],
        'lnnid': [r'LB NID:\s*([\d.]+)'],
        'pais': [r'(MEXICO)'],
        'pe': [r'PTO\s*([^\s,]+)', r'(?<!C)PE:\s*([^\s,]+)', r'PE:\s*([^\s,]+)'],
        'pe_b': [r'(?i)CLIENT_B:\s*(.*?)(?=\n)'],
        'rd': [r'RD:\s*([^\s,]+)'],
        'rfs_ip_port': [r'IP Port:\s*(\d+)', r'IP PORT:\s*(\d+)', r'RFS IP PORT:\s*(\d+)', r'RFS IP Port:\s*(\d+)', r'IP Port :\s*(\d+)', r'(\d+)\s*IP Port\s*', r'\*:\s*RFS(\d+)\s*\( IP Port \)', r'\*:\s*(\d+)\s*\(IP Port\)', r'\*:\s*RFS\s*(\d+)\s*\( IP Port \)', r'RFS IP Port de VPLS - Punta Z:\s*(\d+)'],
        'rfs_ip_port_nid': [r'\*:\s*(\d+)\s*\(NID\)', r'\*:\s*RFS\s*(\d+)\s*\(\s*NID\s*\)', r'\*:\s*RFS\s*(\d+)\s*\( NID \)', r'RFS NID - Punta Z:\s*(\d+)',r'NID\s*:\s*(\d+)',],
        'rfs_ip_port_punta_z': [r'(\d+)\s*\(IP Port\) \| Z LOC', r'RFS IP Port de VPLS - Punta A:\s*(\d+)'],
        'sede': [r'(?i)Site:\s*(.*)', r'(?i)Sede\s*:\s*(.*)', r'(?i)SITE:\s*(.*)'],
        'sede_b': [r'(?i)Z-Side Site:\s*(.*)',],
        'svlan': [r'Int:\s*ae-\d+:(\d+)\.\d+', r'Svlan:\s*(\d+)', r'INT:\s*ae\d+\.(\d+)'],
        'sw': [r'NODO\s*(\d+)', r'SW:\s*([^\s,]+)\s*-\s*TEN GIGA\s*[^\s,]+', r'SW:\s*(\d+)', r'DEVICE:\s*([^\s,]+)', r'SW:\s*([^\s,]+)', r'ME:\s*([^\s,]+)', r'DEVICE:\s*([^\s]+)', r'INTERCONEXION\s*-\s*([^\s,]+)', r'NNI\s*[^\s,]+\s*-\s*([^\s,]+)'],
        'tipo': [r'(VPN)', r'(Internet)', r'(EPL)', r'(EVPL)'],
        'vlan': [r'vlan\s*(\d+)', r'VLAN\s*(\d+)', r'S-VLAN:\s*(\d+)', r'VLAN ASIGNADA:\s*(\d+)'],
        'voz': [r'Voz\s*(\d+)%'],
        'wan': [r'IP_WAN:\s*([\d./]+)', r'WAN:\s*([\d./]+)'],
        'wanv6': [r'WANIPv6:\s*([\da-fA-F:]+/\d+)'],
        'video': [r'Video\s*(\d+)%'],
        'vrf': [r'VRF:\s*(.*)', r'vrf:\s*(.*)'],
        'vrf_init': [r'RD:.*(\d{5})',r'Target: 6745:.*(\d{5})',],

}

    resultados = {clave: buscar_primera_coincidencia(patrones, texto) for clave, patrones in patrones_busqueda.items()}
    
    be = "Bundle-ether10" if resultados['be'] == "ae10" else "bundle_ether11" if resultados['tipo'] == "ae11" else "bundle_ether14" if resultados['tipo'] == "ae14" else "No encontrado"
    tipo_servicio = "ADI" if resultados['tipo'] == "Internet" else "VPN" if resultados['tipo'] == "VPN" else "VPLS" if resultados['tipo'] == "EPL" else "VPLS" if resultados['tipo'] == "EVPL" else "No encontrado"
    tipo_equipo = "ALCATEL" if "ar" in resultados['pe'].lower() else "JUNIPER" if (resultados['pais'] != "No encontrado" and tipo_servicio == "ADI") or ("edge" in resultados['pe'].lower()) or ("EPL" in texto)or ("VPLS" in texto) else "No encontrado"
    vpn = "VPN" if "VPN" in texto else "No encontrado"

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
        if 'Mb' in resultados['bw']:
            resultados['bw'] = int(re.search(r'\d+', resultados['bw']).group())
        elif 'Mbps' in resultados['bw']:
            resultados['bw'] = int(re.search(r'\d+', resultados['bw']).group())
        elif 'Gb' in resultados['bw']:
            resultados['bw'] = int(re.search(r'\d+', resultados['bw']).group()) * 1000
        elif 'Gbps' in resultados['bw']:
            resultados['bw'] = int(re.search(r'\d+', resultados['bw']).group()) * 1000

    

    if resultados['cliente'] != "No encontrado" and resultados['sede'] != "No encontrado":
        cliente_palabras = resultados['cliente'].split()
        sede_palabras = resultados['sede'].split()
        valores_unicos_sede = [palabra for palabra in sede_palabras if palabra not in cliente_palabras]
        resultados['sede'] = ' '.join(valores_unicos_sede) if valores_unicos_sede else "No encontrado"

    if buscar_ufinet_nni(texto):
        resultados['sw'] = "BOGTCLFXNN002"
        resultados['interface_sw'] = "TEN GIGA 0/0/2/1"
    else:
        resultados['interface_sw'] = buscar_sw_int(texto)

    if buscar_LIBERTY_nni(texto):
        resultados['sw'] = "BOGTCLFXNN001"
        resultados['interface_sw'] = "TEN GIGA 0/0/2/3"

    if resultados['pe'] != "No encontrado" and resultados['sw'] == "No encontrado":
        resultados['sw'] = "Conectado a PE"

    if resultados['sede'] != "No encontrado":
        resultados['sede'] = resultados['sede'].lstrip(" -")

    if resultados['sede_b'] == "No encontrado":
        resultados['sede_b'] = ""

    if resultados['rfs_ip_port_nid'] == "No encontrado":
        resultados['rfs_ip_port_nid'] = ""

    if resultados['pe'] == "edge1.bgo2" and resultados['interface_pe'] == "et-0/0/18":
        resultados['interface_pe'] = "ae30"

    if vpn == "VPN":
        tipo_equipo = "JUNIPER"

    if resultados['configuracion'] in ["Alta", "alta"]:
        tipo_configuracion = "Alta"
    elif resultados['configuracion'] in ["ampliación", "ampliacion"]:
        tipo_configuracion = "Ampliacion"
    else:
        tipo_configuracion = "No encontrado"
    
    resultados['tipo_servicio'] = tipo_servicio
    resultados['tipo_equipo'] = tipo_equipo
    resultados['tipo_configuracion'] = tipo_configuracion
    resultados['be'] = be

    if resultados['be'] == "No encontrado":
        resultados['be'] = "1"

    if resultados['asn'] == "No encontrado":
        resultados['asn'] = ""

    if resultados['lbcpe'] == "No encontrado":
        resultados['lbcpe'] = ""

    if resultados['pe_b'] == "No encontrado":
        resultados['pe_b'] = ""

    if resultados['sw'] == "No encontrado":
        resultados['sw'] = ""

    if resultados['vlan'] == "No encontrado":
        resultados['vlan'] = ""

    if resultados['interface_sw'] == "No encontrado":
        resultados['interface_sw'] = ""

    if resultados['lnnid'] == "No encontrado":
        resultados['lnnid'] = ""

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

    if resultados['rfs_ip_port_punta_z'] == "No encontrado":
        resultados['rfs_ip_port_punta_z'] = ""

    if resultados['bw_exchange'] == "No encontrado":
        resultados['bw_exchange'] = "0"

    if resultados['bw_plus'] == "No encontrado":
        resultados['bw_plus'] = "0"

    if resultados['voz'] == "No encontrado":
        resultados['voz'] = "0"

    if resultados['video'] == "No encontrado":
        resultados['video'] = "0"

    if resultados['vrf'] == "No encontrado":
        resultados['vrf'] = ""

    if resultados['tipo'] in ["EPL", "EVPL"]:
        cliente_modificado = resultados['cliente'].replace("&", "").replace(" ", "-")
        resultados['vrf'] = f"{resultados['cfs']}-{cliente_modificado}"
        resultados['rd'] = resultados['cfs']

    if "1114094/1" in texto:
        resultados['pe'] = "PSR1.PRC1"
        resultados['interface_pe'] = "xe-1/0/0"
        resultados['sw'] = "Conectado a PE"
    
    if "CO202100010" in texto:
        resultados['pe_b'] = "psr2.bgo2"
        resultados['interface_pe_b'] = "xe-1/0/9"

    if resultados['vrf_init'] != "No encontrado":
        resultados['vrf_init'] = resultados['vrf_init'].lstrip('0')
        
    ejecutar_enlace(cfs)

    print(json.dumps(resultados))

if __name__ == "__main__":
    cfs = sys.argv[1] if len(sys.argv) > 1 else ""
    main(cfs)