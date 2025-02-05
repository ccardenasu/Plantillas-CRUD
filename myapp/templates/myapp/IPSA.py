import re
import os
import sys
import json
import subprocess

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

    rfs_ip_port_nid_resultado = buscar_primera_coincidencia(r'NID :\s*(\d+)', texto)

# Modificar el patrón de búsqueda para incluir 'VLAN'
    vlan_resultado = buscar_primera_coincidencia(r'VLAN\s*(\d+)', texto)

    # Modificar el patrón de búsqueda para incluir 'DEVICE'
    sw_resultado = buscar_primera_coincidencia(r'DEVICE:\s*([^\s,]+)', texto)

    # Ejecutar el enlace si algún resultado es "No encontrado"
    if cliente_resultado == "No encontrado" or sede_resultado == "No encontrado" or cfs_resultado == "No encontrado" or rfs_ip_port_resultado == "No encontrado":
        ejecutar_enlace(cfs)

    print(json.dumps({
        
        'dko': dko_resultado,
        'cliente': cliente_resultado,
        'sede': sede_resultado,
        'cfs': cfs_resultado,
        'rfs_ip_port': rfs_ip_port_resultado,
        'rfs_ip_port_nid': rfs_ip_port_nid_resultado,
        'vlan': vlan_resultado,
        'sw': sw_resultado,


    }))

if __name__ == "__main__":
    cfs = sys.argv[1] if len(sys.argv) > 1 else ""
    main(cfs)