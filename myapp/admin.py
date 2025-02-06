# myapp/admin.py
from django.contrib import admin
from .models import Datos

class DatosAdmin(admin.ModelAdmin):
    list_display = [
    'IES', 'asn', 'be', 'bundle_ether', 'bundle_ether_b', 'bw', 'bw_Exchange', 'bw_plus', 'cfs', 'child_port', 
    'cliente', 'cv', 'cv_b', 'dko', 'encap_type', 'interface_pe', 'interface_pe_b', 'interface_pe_vpls_a', 
    'interface_pe_vpls_b', 'interface_sw', 'interface_sw_b', 'lag', 'lag_administrative_key', 'lan', 'lanv6', 
    'lb_pe_vpls_a', 'lb_pe_vpls_b', 'lbcpe', 'lnnid', 'mtu', 'pe', 'pe_b', 'pe_vpls_a', 'pe_vpls_b', 'port_breakout', 
    'puertos_lag', 'rd', 'rfs_ip_port', 'rfs_ip_port_b', 'rfs_ip_port_nid', 'root_port', 'sede', 'sede_b', 'sv', 
    'sv_b', 'sw', 'sw_b', 'tipo_configuracion', 'tipo_equipo', 'tipo_servicio', 'unit', 'unit_b', 'unit_nid', 'vrf', 
    'vrf_init','vt', 'wan', 'wanv6'
    ]
    readonly_fields=('created_at','updated_at')
    search_fields = [
    'IES', 'asn', 'be', 'bundle_ether', 'bundle_ether_b', 'bw', 'bw_Exchange', 'bw_plus', 'cfs', 'child_port', 
    'cliente', 'cv', 'cv_b', 'dko', 'encap_type', 'interface_pe', 'interface_pe_b', 'interface_pe_vpls_a', 
    'interface_pe_vpls_b', 'interface_sw', 'interface_sw_b', 'lag', 'lag_administrative_key', 'lan', 'lanv6', 
    'lb_pe_vpls_a', 'lb_pe_vpls_b', 'lbcpe', 'lnnid', 'mtu', 'pe', 'pe_b', 'pe_vpls_a', 'pe_vpls_b', 'port_breakout', 
    'puertos_lag', 'rd', 'rfs_ip_port', 'rfs_ip_port_b', 'rfs_ip_port_nid', 'root_port', 'sede', 'sede_b', 'sv', 
    'sv_b', 'sw', 'sw_b', 'tipo_configuracion', 'tipo_equipo', 'tipo_servicio', 'unit', 'unit_b', 'unit_nid', 'vrf', 
    'vrf_init','vt', 'wan', 'wanv6'
    ]


admin.site.register(Datos, DatosAdmin)