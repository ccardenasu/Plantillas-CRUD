# myapp/admin.py
from django.contrib import admin
from .models import Datos

class DatosAdmin(admin.ModelAdmin):
    list_display =  'cfs', 'dko', 'IES', 'tipo_configuracion', 'tipo_servicio', 'tipo_equipo', 'rfs_ip_port', 'rfs_ip_port_b', 'rfs_ip_port_nid', 'cliente', 'sede', 'sede_b', 'sw', 'interface_sw', 'sw_b', 'interface_sw_b', 'vrf', 'rd', 'unit', 'unit_nid','unit_b','vt', 'sv', 'cv', 'bw', 'bw_plus', 'bw_Exchange', 'wan', 'wanv6', 'asn', 'lan', 'lanv6', 'lbcpe', 'lnnid', 'be', 'bundle_ether', 'pe', 'interface_pe','puertos_lag', 'lag','bundle_ether_b', 'pe_b', 'interface_pe_b'
    readonly_fields = ('created_at', 'updated_at')
    search_fields = 'cfs', 'dko', 'IES', 'tipo_configuracion', 'tipo_servicio', 'tipo_equipo', 'rfs_ip_port', 'rfs_ip_port_b', 'rfs_ip_port_nid', 'cliente', 'sede', 'sede_b', 'sw', 'interface_sw', 'sw_b', 'interface_sw_b', 'vrf', 'rd', 'unit', 'unit_nid', 'unit_b','vt', 'sv', 'cv', 'bw', 'bw_plus', 'bw_Exchange', 'wan', 'wanv6', 'asn', 'lan', 'lanv6', 'lbcpe', 'lnnid', 'be', 'bundle_ether', 'pe', 'interface_pe','puertos_lag', 'lag', 'bundle_ether_b', 'pe_b', 'interface_pe_b'


admin.site.register(Datos, DatosAdmin)