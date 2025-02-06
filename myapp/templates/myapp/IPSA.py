import re
import os
import sys
import json
import subprocess
import ipaddress


def main(cfs):
    # Ruta al archivo de datos usando el valor de CFS
    data_path = os.path.join('data', f'{cfs}.txt')

    # Verificar si el archivo existe
    if not os.path.exists(data_path):
        print(json.dumps({'error': f"El archivo {data_path} no existe."}))
        return

    # Leer el contenido del archivo con codificación 'utf-8'
    try:
        with open(data_path, "r", encoding="utf-8") as file:
            texto = file.read()
    except Exception as e:
        print(json.dumps({'error': f"Error al leer el archivo: {e}"}))
        return

    def buscar_primera_coincidencia(patron, texto):
        """
        Busca la primera coincidencia de un patrón en el texto.
        """
        resultado = re.search(patron, texto)
        return resultado.group(1).strip() if resultado else "No encontrado"

    def ejecutar_enlace(cfs):
        """
        Construye y ejecuta el enlace con el valor de CFS.
        """
        url = f"http://dkvapi.lat.intranet/gpin.html?CFSID={cfs}&ActCountry=MEX&ActUCase=PRO&DVReadOnly=0"
        subprocess.Popen(['wslview', url])

    # Buscar 'Cliente' y 'Sede'
    cliente_resultado = buscar_primera_coincidencia(r'(?i)Cliente:\s*(.*?)(?=\n\S)', texto)
    if cliente_resultado == "No encontrado":
        cliente_resultado = buscar_primera_coincidencia(r'(?i)CLIENTE:\s*(.*?)(?=\n\S)', texto)
    
    sede_resultado = buscar_primera_coincidencia(r'(?i)Sede:\s*(.*)', texto)

    # Reemplazar "Ñ" por "N" en los resultados
    cliente_resultado = cliente_resultado.replace("Ñ", "N")
    if sede_resultado != "No encontrado":
        sede_resultado = sede_resultado.replace("Ñ", "N")

    # Eliminar la parte común entre Cliente y Sede
    if cliente_resultado in sede_resultado:
        sede_resultado = sede_resultado.replace(cliente_resultado, "").strip(" -")
    else:
        cliente_palabras = cliente_resultado.split()
        for palabra in cliente_palabras:
            if palabra in sede_resultado:
                sede_resultado = sede_resultado.replace(palabra, "").strip(" -")

    dko_resultado = buscar_primera_coincidencia(r'DKO:\s*(\d+)', texto)

    cfs_resultado = buscar_primera_coincidencia(r'CID-CFS :\s*(\d+)', texto)
    if cfs_resultado == "No encontrado":
        cfs_resultado = buscar_primera_coincidencia(r'CFS-CID:\s*(\d+)', texto)
    if cfs_resultado == "No encontrado":
        cfs_resultado = buscar_primera_coincidencia(r'CID-CFS:\s*(\d+)', texto)
    if cfs_resultado == "No encontrado":
        cfs_resultado = buscar_primera_coincidencia(r'CFS:\s*(\d+)', texto)
    if cfs_resultado == "No encontrado":
        cfs_resultado = buscar_primera_coincidencia(r'CFS\s*(\d+)', texto)

    rfs_ip_port_resultado = buscar_primera_coincidencia(r'RFS IP PORT:\s*(\d+)', texto)
    if rfs_ip_port_resultado == "No encontrado":
        rfs_ip_port_resultado = buscar_primera_coincidencia(r'RFS IP Port:\s*(\d+)', texto)
    if rfs_ip_port_resultado == "No encontrado":
        rfs_ip_port_resultado = buscar_primera_coincidencia(r'IP Port :\s*(\d+)', texto)
    if rfs_ip_port_resultado == "No encontrado":
        rfs_ip_port_resultado = buscar_primera_coincidencia(r'(\d+)\s*IP Port\s*', texto)
    if rfs_ip_port_resultado == "No encontrado":
        rfs_ip_port_resultado = buscar_primera_coincidencia(r'\*:\s*RFS(\d+)\s*\( IP Port \)', texto)
    if rfs_ip_port_resultado == "No encontrado":
        rfs_ip_port_resultado = buscar_primera_coincidencia(r'\*:\s*(\d+)\s*\(IP Port\)', texto)

    rfs_ip_port_nid_resultado = buscar_primera_coincidencia(r'NID :\s*(\d+)', texto)
    if rfs_ip_port_nid_resultado == "No encontrado":
        rfs_ip_port_nid_resultado = buscar_primera_coincidencia(r'NID:\s*(\d+)', texto)
    if rfs_ip_port_nid_resultado == "No encontrado":
        rfs_ip_port_nid_resultado = buscar_primera_coincidencia(r'\*:\s*(\d+)\s*\(NID\)', texto)


# Modificar el patrón de búsqueda para incluir 'VLAN'
    vlan_resultado = buscar_primera_coincidencia(r'VLAN\s*(\d+)', texto)
    if vlan_resultado == "No encontrado":
        vlan_resultado = buscar_primera_coincidencia(r'VLAN ASIGNADA:\s*(\d+)', texto)
    # Modificar el patrón de búsqueda para incluir 'DEVICE'
    sw_resultado = buscar_primera_coincidencia(r'DEVICE:\s*([^\s,]+)', texto)
    if sw_resultado == "No encontrado":
        sw_resultado = buscar_primera_coincidencia(r'SW:\s*([^\s,]+)', texto)
    if sw_resultado == "No encontrado":
        sw_resultado = buscar_primera_coincidencia(r'DEVICE:\s*([^\s]+)', texto)

    # Ajustar el patrón de búsqueda para "bw"
    bw_resultado = buscar_primera_coincidencia(r'@(\d+)([MG]b)', texto)

    # Buscar 'bw'
    bw_resultado = buscar_primera_coincidencia(r'@(\d+[MG]b)', texto)
    if bw_resultado != "No encontrado":
        match = re.match(r'(\d+)([MG]b)', bw_resultado)
        if match:
            bw_valor, unidad = match.groups()
            bw_valor = int(bw_valor)
            if unidad == "Gb":
                bw_valor *= 1000  # Convertir gigabits a megabits
            bw_resultado = f"{bw_valor}"
    else:
        bw_resultado = "No encontrado"
    # Ajustar el patrón de búsqueda para "DEVICE" con el estándar especificado
    interface_sw_resultado = buscar_primera_coincidencia(r'DEVICE:\s*[^\s,]+\s+(Te\d+/\d+/\d+/\d+)', texto)

     # Buscar 'vrf'
    vrf_resultado = buscar_primera_coincidencia(r'VRF:\s*(.*)', texto)

     # Buscar 'asn'
    asn_resultado = buscar_primera_coincidencia(r'AS_BGP:\s*(\d+)', texto)

        # Buscar 'wan'
    wan_resultado = buscar_primera_coincidencia(r'IP_WAN:\s*([\d./]+)', texto)
    if wan_resultado != "No encontrado":
        try:
            ip_network = ipaddress.ip_network(wan_resultado, strict=False)
            wan_resultado = str(ip_network.network_address) + '/' + str(ip_network.prefixlen)
        except ValueError as e:
            wan_resultado = f"Error al convertir IP: {e}"

    # Buscar 'lbcpe'
    lbcpe_resultado = buscar_primera_coincidencia(r'CPE :\s*(\d+)', texto)

    # Ejecutar el enlace si algún resultado es "No encontrado"
    if cliente_resultado == "No encontrado" or rfs_ip_port_nid_resultado != "No encontrado" or sede_resultado == "No encontrado" or cfs_resultado == "No encontrado" or rfs_ip_port_resultado == "No encontrado" or rfs_ip_port_nid_resultado == "No encontrado":
        ejecutar_enlace(cfs)

    print(json.dumps({
        
        'lbcpe': lbcpe_resultado,
        'wan': wan_resultado,
        'asn': asn_resultado,
        'vrf': vrf_resultado,
        'dko': dko_resultado,
        'cliente': cliente_resultado,
        'sede': sede_resultado,
        'cfs': cfs_resultado,
        'rfs_ip_port': rfs_ip_port_resultado,
        'rfs_ip_port_nid': rfs_ip_port_nid_resultado,
        'vlan': vlan_resultado,
        'sw': sw_resultado,
        'interface_sw': interface_sw_resultado,
        'bw': bw_resultado,
        'lnnid':rfs_ip_port_nid_resultado,

        




    }))

if __name__ == "__main__":
    cfs = sys.argv[1] if len(sys.argv) > 1 else ""
    main(cfs)