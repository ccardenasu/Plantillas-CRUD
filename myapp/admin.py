# myapp/admin.py
from django.contrib import admin
from .models import Datos

class DatosAdmin(admin.ModelAdmin):
    list_display =  'cfs', 'dko', 'tipo_configuracion', 'tipo_servicio', 'rfs_ip_port', 'cliente', 'sede', 'sede_b', 'sw', 'interface_sw', 'sw_b', 'interface_sw_b', 'vrf', 'rd', 'unit', 'unit_b','vt', 'sv', 'cv', 'bw', 'wan', 'wanv6', 'asn', 'lan', 'lbcpe', 'lnnid', 'bundle_ether', 'pe', 'interface_pe', 'bundle_ether_b', 'pe_b', 'interface_pe_b'
    readonly_fields = ('created_at', 'updated_at')
    search_fields = 'cfs', 'dko', 'tipo_configuracion', 'tipo_servicio', 'rfs_ip_port', 'cliente', 'sede', 'sede_b', 'sw', 'interface_sw', 'sw_b', 'interface_sw_b', 'vrf', 'rd', 'unit', 'unit_b','vt', 'sv', 'cv', 'bw', 'wan', 'wanv6', 'asn', 'lan', 'lbcpe', 'lnnid', 'bundle_ether', 'pe', 'interface_pe', 'bundle_ether_b', 'pe_b', 'interface_pe_b'


admin.site.register(Datos, DatosAdmin)