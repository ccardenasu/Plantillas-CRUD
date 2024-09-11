from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .forms import DatosForm
from .models import Datos
import os
import ipaddress
import csv


def datos_view(request):
    if request.method == 'POST':
        form = DatosForm(request.POST)
        if form.is_valid():
            datos = form.save(commit=False)
            num_puertos_lag = form.cleaned_data.get('num_puertos_lag')
            # Puedes usar num_puertos_lag aquí según sea necesario
            datos.save()
            # Asegurarse de que el directorio 'media' existe
            media_dir = os.path.join(os.path.dirname(__file__), '..', 'media')
            if not os.path.exists(media_dir):
                os.makedirs(media_dir)
            # Generar el archivo TXT
            file_path = os.path.join(media_dir, f'{datos.cfs}.txt')
            try:
                with open(file_path, 'w') as file:
                    def write_if_not_none(field_name, field_value):
                        if field_value not in [None, '']:
                            file.write(f'{field_name}: {field_value}\n')
                    write_if_not_none('CFS', datos.cfs)
                    write_if_not_none('Tipo de configuración', datos.tipo_configuracion)
                    write_if_not_none('Tipo de equipo', datos.tipo_equipo)
                    write_if_not_none('RFS-IP-PORT', datos.rfs_ip_port)
                    write_if_not_none('RFS-IP-PORT_B', datos.rfs_ip_port_b)
                    write_if_not_none('Cliente', datos.cliente)
                    write_if_not_none('bundle_ether', datos.bundle_ether)
                    write_if_not_none('bundle_ether_b', datos.bundle_ether_b)
                    write_if_not_none('SEDE', datos.sede)
                    write_if_not_none('SEDE_B', datos.sede_b)
                    write_if_not_none('DKO', datos.dko)
                    write_if_not_none('SW', datos.sw)
                    write_if_not_none('Interface SW', datos.interface_sw)
                    write_if_not_none('SW_B', datos.sw_b)
                    write_if_not_none('Interface SW_B', datos.interface_sw_b)
                    write_if_not_none('PE', datos.pe)
                    write_if_not_none('Interface PE', datos.interface_pe)
                    write_if_not_none('puertos_lag', datos.puertos_lag)
                    write_if_not_none('PE_B', datos.pe_b)
                    write_if_not_none('Interface PE_B', datos.interface_pe_b)
                    write_if_not_none('VRF', datos.vrf)
                    write_if_not_none('RD', datos.rd)
                    write_if_not_none('Unit', datos.unit)
                    write_if_not_none('Unit_b', datos.unit_b)
                    write_if_not_none('VT', datos.vt)
                    write_if_not_none('SV', datos.sv)
                    write_if_not_none('CV', datos.cv)
                    write_if_not_none('BW', datos.bw)
                    write_if_not_none('WAN', datos.wan)
                    write_if_not_none('WANv6', datos.wanv6)
                    write_if_not_none('ASN', datos.asn)
                    write_if_not_none('LAN', datos.lan)
                    write_if_not_none('LBCPE', datos.lbcpe)
                    write_if_not_none('LNNID', datos.lnnid)
                    write_if_not_none('Fecha de creación', datos.created_at)

                    # Comandos adicionales...
                    network = ipaddress.IPv4Network(datos.wan, strict=False)
                    first_host_ip = str(network.network_address + 1)
                    file.write(f'set interfaces {datos.interface_pe} unit {datos.unit} family inet address {first_host_ip}/{network.prefixlen}\n')
                    file.write(f'set interfaces {datos.interface_pe} unit {datos.unit} disable\n')
                    file.write(f'deactivate interfaces {datos.interface_pe} unit {datos.unit}\n')
            except Exception as e:
                return HttpResponse(f"Error al crear el archivo: {e}")

            # Calcular BWx1024, delay-buffer-rate, y shaping-rate
            try:
                bw = int(datos.bw)
                bwx1024 = int(bw * 1024)
                delay_buffer_rate = bw * 1024 * 1000 * 4
                shaping_rate = bw * 1024 * 1000
                burst_size_limit =  int(bw * 1024 * 1000 * 0.15 / 4)
            except ValueError:
                bwx1024 = None
                delay_buffer_rate = None
                shaping_rate = None
                burst_size_limit = None

            return render(request, 'myapp/datos_guardados.html', {
                'datos': datos,
                'BWx1024': bwx1024,
                'delay_buffer_rate': delay_buffer_rate,
                'shaping_rate': shaping_rate,
                'burst_size_limit': burst_size_limit
            })
    else:
        form = DatosForm()

    return render(request, 'myapp/capturar_datos.html', {'form': form})

def buscar_cfs(request):
    cfs = request.GET.get('cfs', None)
    if cfs:
        try:
            datos = Datos.objects.filter(cfs=cfs)
            if datos.exists():
                data = {
                    'exists': True,
                    'records': [
                        {
                            'id': dato.id,
                            'tipo_servicio': dato.tipo_servicio,
                            'tipo_equipo': dato.tipo_equipo,
                            'tipo_configuracion': dato.tipo_configuracion,
                            'rfs_ip_port': dato.rfs_ip_port,
                            'rfs_ip_port_b': dato.rfs_ip_port_b,
                            'cliente': dato.cliente,
                            'bundle_ether': dato.bundle_ether,
                            'bundle_ether_b': dato.bundle_ether_b,
                            'sede': dato.sede,
                            'sede_b': dato.sede_b,
                            'dko': dato.dko,
                            'sw': dato.sw,
                            'interface_sw': dato.interface_sw,
                            'sw_b': dato.sw_b,
                            'interface_sw_b': dato.interface_sw_b,
                            'pe': dato.pe,
                            'interface_pe': dato.interface_pe,
                            'puertos_lag': dato.puertos_lag,
                            'pe_b': dato.pe_b,
                            'interface_pe_b': dato.interface_pe_b,
                            'vrf': dato.vrf,
                            'rd': dato.rd,
                            'unit': dato.unit,
                            'unit_b': dato.unit_b,
                            'vt': dato.vt,
                            'sv': dato.sv,
                            'cv': dato.cv,
                            'bw': dato.bw,
                            'wan': dato.wan,
                            'wanv6': dato.wanv6,
                            'asn': dato.asn,
                            'lan': dato.lan,
                            'lbcpe': dato.lbcpe,
                            'lnnid': dato.lnnid,
                            'created_at': dato.created_at.strftime('%Y-%m-%d %H:%M:%S'),  # Incluir fecha de creación
                        } for dato in datos
                    ]
                }
            else:
                data = {'exists': False}
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        data = {'exists': False}
    return JsonResponse(data)

def buscar_en_csv(request):
    term = request.GET.get('term', None)
    if term:
        csv_file_path = os.path.join(settings.BASE_DIR, 'myapp/Metro.csv')
        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                for row in reader:
                    if row[0] == term:
                        return JsonResponse({'found': True, 'value1': row[7], 'value2': row[6], 'value3': row[8]})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'found': False})