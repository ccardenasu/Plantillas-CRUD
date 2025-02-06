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
        'configuracion': [r'(Alta)'],
        'pais': [r'(MEXICO)'],
        'cliente': [r'(?i)Cliente:\s*(.*?)(?=\n\S)', r'(?i)CLIENTE:\s*(.*?)(?=\n\S)'],
        'sede': [r'(?i)Sede:\s*(.*)'],
        'dko': [r'DKO:\s*(\d+)'],
        'cfs': [r'CID-CFS :\s*(\d+)', r'CFS-CID:\s*(\d+)', r'CID-CFS:\s*(\d+)', r'CFS:\s*(\d+)', r'CFS\s*(\d+)'],
        'rfs_ip_port': [r'RFS IP PORT:\s*(\d+)', r'RFS IP Port:\s*(\d+)', r'IP Port :\s*(\d+)', r'(\d+)\s*IP Port\s*', r'\*:\s*RFS(\d+)\s*\( IP Port \)', r'\*:\s*(\d+)\s*\(IP Port\)'],
        'rfs_ip_port_nid': [r'NID :\s*(\d+)', r'NID:\s*(\d+)', r'\*:\s*(\d+)\s*\(NID\)'],
        'vlan': [r'VLAN\s*(\d+)', r'VLAN ASIGNADA:\s*(\d+)'],
        'sw': [r'DEVICE:\s*([^\s,]+)', r'SW:\s*([^\s,]+)', r'DEVICE:\s*([^\s]+)'],
        'bw': [r'@(\d+[MG]b)'],
        'interface_sw': [r'DEVICE:\s*[^\s,]+\s+(Te\d+/\d+/\d+/\d+)'],
        'vrf': [r'VRF:\s*(.*)'],
        'asn': [r'AS_BGP:\s*(\d+)'],
        'wan': [r'IP_WAN:\s*([\d./]+)'],
        'lbcpe': [r'CPE :\s*(\d+)'],
        'tipo': [r'(Internet)'],
    }

    resultados = {clave: buscar_primera_coincidencia(patrones, texto) for clave, patrones in patrones_busqueda.items()}

    if resultados['wan'] != "No encontrado":
        try:
            ip_network = ipaddress.ip_network(resultados['wan'], strict=False)
            resultados['wan'] = str(ip_network.network_address) + '/' + str(ip_network.prefixlen)
        except ValueError as e:
            resultados['wan'] = f"Error al convertir IP: {e}"

    if resultados['bw'] != "No encontrado":
        match = re.match(r'(\d+)([MG]b)', resultados['bw'])
        if match:
            bw_valor, unidad = match.groups()
            bw_valor = int(bw_valor)
            if unidad == "Gb":
                bw_valor *= 1000
            resultados['bw'] = f"{bw_valor}"

    # Asignar "ADI" a tipo_servicio si se encuentra "Internet"
    tipo_servicio = "ADI" if resultados['tipo'] != "No encontrado" else "No encontrado"

    # Asignar "Juniper" a tipo_equipo si se encuentra "MEXICO" y tipo_servicio es "ADI"
    tipo_equipo = "JUNIPER" if resultados['pais'] != "No encontrado" and tipo_servicio == "ADI" else "No encontrado"

    # Asignar "Alta" a tipo_configuracion si se encuentra "Alta"
    tipo_configuracion = "Alta" if resultados['configuracion'] != "No encontrado" else "No encontrado"

    if any(resultados[clave] == "No encontrado" for clave in ['cliente', 'sede', 'cfs', 'rfs_ip_port', 'rfs_ip_port_nid']):
        ejecutar_enlace(cfs)

    resultados['tipo_servicio'] = tipo_servicio
    resultados['tipo_equipo'] = tipo_equipo
    resultados['tipo_configuracion'] = tipo_configuracion


    print(json.dumps(resultados))

if __name__ == "__main__":
    cfs = sys.argv[1] if len(sys.argv) > 1 else ""
    main(cfs)