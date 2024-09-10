# myapp/admin.py
from django.contrib import admin
from .models import Datos

class DatosAdmin(admin.ModelAdmin):
    list_display =  ('cfs', 'bundle_ether', 'bundle_ether_b', 'dko', 'sw', 'interface_sw', 'sw_b', 'interface_sw_b', 'pe', 'interface_pe', 'pe_b', 'interface_pe_b', 'vrf', 'rd', 'unit', 'unit_b', 'vt', 'sv', 'cv', 'bw', 'wan', 'wanv6', 'asn', 'lan', 'lbcpe', 'lnnid', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('cfs', 'bundle_ether', 'bundle_ether_b', 'dko', 'sw', 'interface_sw', 'sw_b', 'interface_sw_b', 'pe', 'interface_pe', 'pe_b', 'interface_pe_b', 'vrf', 'rd', 'unit', 'unit_b', 'vt', 'sv', 'cv', 'bw', 'wan', 'wanv6', 'asn', 'lan', 'lbcpe', 'lnnid', 'created_at', 'updated_at')

admin.site.register(Datos, DatosAdmin)