from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .forms import DatosForm
from .models import Datos
import os
import ipaddress
import csv
import subprocess
import json  # Asegúrate de importar el módulo json
from django.views.decorators.csrf import csrf_exempt


def ejecutar_ipsa(request):
    cfs = request.GET.get('cfs', '')
    try:
        # Actualiza la ruta al archivo IPSA.py
        result = subprocess.run(['python', '/home/carlos/githut/Plantillas-CRUD/myapp/templates/myapp/IPSA.py', cfs], capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout.strip()
            data = json.loads(output)
            return JsonResponse({'success': True, 'data': data})
        else:
            return JsonResponse({'success': False, 'error': result.stderr})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

def datos_view(request):
    if request.method == "POST":
        form = DatosForm(request.POST)
        if form.is_valid():
            datos = form.save(commit=False)
            num_puertos_lag = form.cleaned_data.get("num_puertos_lag")
            datos.save()

            lan_ips = [ip.strip() for ip in datos.lan.split(',')]
            lanv6_ips = [ip.strip() for ip in datos.lanv6.split(',')] if datos.lanv6 else []
            lan_ips_with_masks = [(ip.strip(), ipaddress.ip_network(ip.strip(), strict=False).prefixlen) for ip in datos.lan.split(',')] if datos.lan else []
            lanv6_ips_with_masks = [(ip.strip(), ipaddress.ip_network(ip.strip(), strict=False).prefixlen) for ip in datos.lanv6.split(',')] if datos.lanv6 else []

            # Asegurarse de que el directorio 'media' existe
            media_dir = os.path.join(os.path.dirname(__file__), "..", "media")
            if not os.path.exists(media_dir):
                os.makedirs(media_dir)
            # Generar el archivo TXT
            file_path = os.path.join(media_dir, f"{datos.cfs}.txt")
            try:
                with open(file_path, "w") as file:

                    def write_if_not_none(field_name, field_value):
                        if field_value not in [None, ""]:
                            file.write(f"{field_name}: {field_value}\n")
                            
                            write_if_not_none("asn", datos.asn)
                            write_if_not_none("be", datos.be)
                            write_if_not_none("bw", datos.bw)
                            write_if_not_none("bw_plus", datos.bw_plus)
                            write_if_not_none("bw_exchenge", datos.bw_exchange)
                            write_if_not_none("bundle_ether", datos.bundle_ether)
                            write_if_not_none("bundle_ether_b", datos.bundle_ether_b)
                            write_if_not_none("cfs", datos.cfs)
                            write_if_not_none("cliente", datos.cliente)
                            write_if_not_none("cv", datos.cv)
                            write_if_not_none("cv_b", datos.cv_b)
                            write_if_not_none("dko", datos.dko)
                            write_if_not_none("fecha de creación", datos.created_at)
                            write_if_not_none("ies", datos.ies)
                            write_if_not_none("interface pe", datos.interface_pe)
                            write_if_not_none("interface pe_b", datos.interface_pe_b)
                            write_if_not_none("interface pe_vpls_a", datos.interface_pe_vpls_a)
                            write_if_not_none("interface pe_vpls_b", datos.interface_pe_vpls_b)
                            write_if_not_none("interface sw", datos.interface_sw)
                            write_if_not_none("interface sw_b", datos.interface_sw_b)
                            write_if_not_none("lan", datos.lan)
                            write_if_not_none("lanv6", datos.lanv6)
                            write_if_not_none("lbcpe", datos.lbcpe)
                            write_if_not_none("lnnid", datos.lnnid)
                            write_if_not_none("lag", datos.lag)
                            write_if_not_none("pe", datos.pe)
                            write_if_not_none("pe_b", datos.pe_b)
                            write_if_not_none("pe_vpls_a", datos.pe_vpls_a)
                            write_if_not_none("pe_vpls_b", datos.pe_vpls_b)
                            write_if_not_none("puertos_lag", datos.puertos_lag)
                            write_if_not_none("rfs-ip-port", datos.rfs_ip_port)
                            write_if_not_none("rfs-ip-port_b", datos.rfs_ip_port_b)
                            write_if_not_none("rfs-ip-port_nid", datos.rfs_ip_port_nid)
                            write_if_not_none("rd", datos.rd)
                            write_if_not_none("sede", datos.sede)
                            write_if_not_none("sede_b", datos.sede_b)
                            write_if_not_none("sv", datos.sv)
                            write_if_not_none("sw", datos.sw)
                            write_if_not_none("sw_b", datos.sw_b)
                            write_if_not_none("tipo de configuración", datos.tipo_configuracion)
                            write_if_not_none("tipo de equipo", datos.tipo_equipo)
                            write_if_not_none("unit", datos.unit)
                            write_if_not_none("unit_nid", datos.unit_nid)
                            write_if_not_none("unit_b", datos.unit_b)
                            write_if_not_none("vrf", datos.vrf)
                            write_if_not_none("vrf_init", datos.vrf_init)
                            write_if_not_none("vt", datos.vt)
                            write_if_not_none("wan", datos.wan)
                            write_if_not_none("wanv6", datos.wanv6)
                            write_if_not_none("child_port", datos.child_port)
                            write_if_not_none("encap_type", datos.encap_type)
                            write_if_not_none("mtu", datos.mtu)
                            write_if_not_none("port_breakout", datos.port_breakout)
                            write_if_not_none("root_port", datos.root_port)


                    # Comandos adicionales...
                    network = ipaddress.IPv4Network(datos.wan, strict=False)
                    first_host_ip = str(network.network_address + 1)
                    file.write(
                        f"set interfaces {datos.interface_pe} unit {datos.unit} family inet address {first_host_ip}/{network.prefixlen}\n"
                    )
                    file.write(
                        f"set interfaces {datos.interface_pe} unit {datos.unit} disable\n"
                    )
                    file.write(
                        f"deactivate interfaces {datos.interface_pe} unit {datos.unit}\n"
                    )
            except Exception as e:
                return HttpResponse(f"Error al crear el archivo: {e}")

            # Calcular BWx1024, delay-buffer-rate, y shaping-rate
            try:
                bw = int(datos.bw)
                print(f"bw {bw}")
                bwx1024 = int(bw * 1024)
                print(f"bwx1024 {bwx1024}")
                bwjun = int(bw * 1000 * 1000)
                print(f"bwjun {bwjun}")
                delay_buffer_rate = bw * 1024 * 1000 * 4
                print(f"delay_buffer_rate {delay_buffer_rate}")
                shaping_rate = bw * 1024 * 1000
                print(f"shaping_rate {shaping_rate}")
                burst_size_limit = int(bw * 1024 * 1000 * 0.15 / 4)
                print(f"burst_size_limit {burst_size_limit}")
                bw_plus_por = round(int(datos.bw_plus)*bwjun / 100)
                print(f"bw_plus_por {bw_plus_por}")
                bw_exchange_por = round(int(datos.bw_exchange )*bwjun / 100)
                print(f"bw_exchange_por {bw_exchange_por}")
                burst_size_limit_plus = round((bwx1024 * 1000 * (int(datos.bw_plus ) / 100*0.15/4)))
                print(f"burst_size_limit_plus {burst_size_limit_plus}")
                burst_size_limit_Exchange = round((bwx1024 * 1000 * (int(datos.bw_exchange ) / 100*0.15/4)))
                print(f"burst_size_limit_exchange {burst_size_limit_Exchange}")
                bw_lag_alcatel = int(datos.puertos_lag) * bwx1024
                print(f"bw_lag_alcatel {bw_lag_alcatel}")
                qos = str(bw_lag_alcatel)[:1]  # Extrae los dos primeros dígitos
                print(f"qos: {qos}")
            except ValueError:
                bwx1024 = None
                bwjun = None
                delay_buffer_rate = None
                shaping_rate = None
                burst_size_limit = None
                bw_lag_alcatel = None
                qos = None
                bw_plus_por = None
                bw_exchange_por = None
                burst_size_limit_plus = None
                burst_size_limit_Exchange = None
            
            form.fields['lag'].initial = num_puertos_lag
            
            return render(
                request,
                "myapp/datos_guardados.html",
                {
                    "datos": datos,
                    "form": form,
                    "num_puertos_lag": num_puertos_lag,
                    "bwjun": bwjun,
                    "BWx1024": bwx1024,
                    "delay_buffer_rate": delay_buffer_rate,
                    "shaping_rate": shaping_rate,
                    "burst_size_limit": burst_size_limit,
                    "bw_lag_alcatel": bw_lag_alcatel,
                    "bw_plus_por": bw_plus_por,
                    "bw_exchange_por": bw_exchange_por,
                    "burst_size_limit_plus": burst_size_limit_plus,
                    "burst_size_limit_Exchange": burst_size_limit_Exchange,
                    "qos": qos,
                    "lan_ips": lan_ips,  # Pasar las IPs procesadas a la plantilla
                    "lanv6_ips": lanv6_ips,  # Pasar las IPs procesadas a la plantilla
                    "lan_ips_with_masks": lan_ips_with_masks,  # Pasar las IPs y sus máscaras a la plantilla
                    "lanv6_ips_with_masks": lanv6_ips_with_masks,  # Pasar las IPs y sus máscaras a la plantilla

                },
            )
    else:
        form = DatosForm()

    return render(request, "myapp/capturar_datos.html", {"form": form})


from django.http import JsonResponse

def buscar_cfs(request):
    cfs = request.GET.get("cfs", None)
    if cfs:
        try:
            datos = Datos.objects.filter(cfs=cfs)
            if datos.exists():
                data = {
                    "exists": True,
                    "records": [
                        {
                            "asn": dato.asn,
                            "bundle_ether": dato.bundle_ether,
                            "bundle_ether_b": dato.bundle_ether_b,
                            "be": dato.be,
                            "bw": dato.bw,
                            "bw_bw_plus": dato.bw_plus,
                            "bw_bw_exchange": dato.bw_exchange,
                            "cfs": dato.cfs,
                            "cliente": dato.cliente,
                            "cv": dato.cv,
                            "cv_b": dato.cv_b,
                            "dko": dato.dko,
                            "id": dato.id,
                            "ies": dato.ies,
                            "interface_pe": dato.interface_pe,
                            "interface_pe_vpls_a": dato.interface_pe_vpls_a,
                            "interface_pe_vpls_b": dato.interface_pe_vpls_b,
                            "interface_pe_b": dato.interface_pe_b,
                            "interface_sw": dato.interface_sw,
                            "interface_sw_b": dato.interface_sw_b,
                            "lan": dato.lan,
                            "lanv6": dato.lanv6,
                            "lag": dato.lag,
                            "lbcpe": dato.lbcpe,
                            "lnnid": dato.lnnid,
                            "pe": dato.pe,
                            "pe_vpls_a": dato.pe_vpls_a,
                            "pe_vpls_b": dato.pe_vpls_b,
                            "lb_pe_vpls_a": dato.lb_pe_vpls_a,
                            "lb_pe_vpls_b": dato.lb_pe_vpls_b,
                            "pe_b": dato.pe_b,
                            "puertos_lag": dato.puertos_lag,
                            "rd": dato.rd,
                            "rfs_ip_port": dato.rfs_ip_port,
                            "rfs_ip_port_b": dato.rfs_ip_port_b,
                            "rfs_ip_port_nid": dato.rfs_ip_port_nid,
                            "sede": dato.sede,
                            "sede_b": dato.sede_b,
                            "sv": dato.sv,
                            "sv_b": dato.sv_b,
                            "sw": dato.sw,
                            "sw_b": dato.sw_b,
                            "tipo_configuracion": dato.tipo_configuracion,
                            "tipo_equipo": dato.tipo_equipo,
                            "tipo_servicio": dato.tipo_servicio,
                            "unit": dato.unit,
                            "unit_nid": dato.unit_nid,
                            "unit_b": dato.unit_b,
                            "vrf": dato.vrf,
                            "vt": dato.vt,
                            "wan": dato.wan,
                            "wanv6": dato.wanv6,
                            "port_breakout": dato.port_breakout,
                            "root_port": dato.root_port,
                            "child_port": dato.child_port,
                            "encap_type": dato.encap_type,
                            "mtu": dato.mtu,
                            "lag_administrative_key": dato.lag_administrative_key,
                            "created_at": dato.created_at.strftime("%Y-%m-%d %H:%M:%S")  # Incluir fecha de creación
                        }
                        for dato in datos
                    ],
                }
            else:
                data = {"exists": False}
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        data = {"exists": False}
    return JsonResponse(data)



def buscar_en_csv(request):
    term = request.GET.get("term", None)
    if term:
        csv_file_path = os.path.join(settings.BASE_DIR, "myapp/Metro.csv")
        try:
            with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile, delimiter=";")
                for row in reader:
                    if row[0] == term:
                        return JsonResponse(
                            {
                                "found": True,
                                "value1": row[7],
                                "value2": row[6],
                                "value3": row[8],
                                "value4": row[9],
                                "value5": row[10],
                                "value6": row[12],
                                "value7": row[13],
                                "value8": row[11],
                                "value9": row[14],
                            }
                        )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"found": False})

def buscar_vrf_page(request):
    return render(request, 'myapp/buscar_vrf.html')

import os
import csv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def buscar_vrf_rd(request):
    if request.method == "GET":
        vrf = request.GET.get("vrf", None)
        print(f"VRF recibido: {vrf}")
        if vrf:
            csv_file_path = os.path.join(settings.BASE_DIR, "myapp/vrf_rd.csv")
            print(f"Ruta del archivo CSV: {csv_file_path}")
            try:
                with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
                    reader = csv.reader(csvfile, delimiter=";")
                    for row in reader:
                        if row[0].strip() == vrf.strip():
                            print(f"VRF encontrado: {vrf}, RD: {row[1]}")
                            return JsonResponse({"found": True, "rd": row[1]})
            except Exception as e:
                print(f"Error al leer el archivo CSV: {e}")
                return JsonResponse({"error": str(e)}, status=500)
            return JsonResponse({"found": False, "message": "VRF no encontrada. Por favor, proporcione el campo 'rd' en una solicitud POST."})
        return JsonResponse({"found": False, "message": "No se proporcionó VRF."})
    
    elif request.method == "POST":
        vrf = request.POST.get("vrf", None)
        rd = request.POST.get("rd", None)
        print(f"VRF recibido: {vrf}, RD recibido: {rd}")
        if vrf and rd:
            csv_file_path = os.path.join(settings.BASE_DIR, "myapp/vrf_rd.csv")
            print(f"Ruta del archivo CSV: {csv_file_path}")
            try:
                with open(csv_file_path, 'a', newline="", encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile, delimiter=";")
                    writer.writerow([vrf, rd])
                    print(f"VRF y RD guardados: {vrf}, {rd}")
                    return JsonResponse({"saved": True, "message": "VRF y RD guardados correctamente."})
            except Exception as e:
                print(f"Error al escribir en el archivo CSV: {e}")
                return JsonResponse({"error": str(e)}, status=500)
        return JsonResponse({"saved": False, "message": "No se proporcionó VRF o RD."})


def pais_mercado_nodo(request):
    if request.method == "POST":
        # Procesar el formulario si es necesario
        pass
    return render(request, 'myapp/pais_mercado_nodo.html')


def buscar_nodo(request):
    resultados = []  # Cambiar a una lista para almacenar todas las coincidencias
    headers = []
    if request.method == 'POST':
        nodo_seleccionado = request.POST.get('nodo')
        sfp_seleccionado = request.POST.get('sfp')
        csv_file = 'myapp/Interface_Equipos.csv'

        try:
            with open(csv_file, mode='r', encoding='latin1') as file:
                reader = csv.reader(file, delimiter=';')
                headers = next(reader)  # Leer la primera fila como encabezados
                for row in reader:
                    row = [col.strip() for col in row]
                    if len(row) > 11:  # Verificar que la fila tenga al menos 12 columnas
                        try:
                            # Verificar las condiciones de filtrado
                            if (row[2] == nodo_seleccionado and 
                                row[10].strip().lower() == 'fisica' and 
                                row[11].strip().lower() == 'shutdown' and 
                                row[9] == sfp_seleccionado):  # Suponiendo que la columna SFP es la 10
                                resultados.append(row)
                        except IndexError as e:
                            print(f"Error de índice: {e} en la fila: {row}")
        except FileNotFoundError:
            print(f"Archivo no encontrado: {csv_file}")
        except UnicodeDecodeError as e:
            print(f"Error de decodificación: {e}")

    return render(request, 'myapp/resultado.html', {'resultados': resultados, 'headers': headers})

def buscar_en_csv_tipo_servicio_sw(request):
    term = request.GET.get("term", None)
    if term:
        csv_file_path = os.path.join(settings.BASE_DIR, "myapp/Metro.csv")
        try:
            with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile, delimiter=";")
                for row in reader:
                    if row[1] == term:
                        return JsonResponse(
                            {
                                "found": True,
                                "value5": row[5],
                                "bundle_ether": row[5],  # Suponiendo que el valor de bundle_ether está en la columna 6

                            }
                        )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"found": False})
