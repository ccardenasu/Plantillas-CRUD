# myapp/admin.py
from django.contrib import admin
from .models import Datos

class DatosAdmin(admin.ModelAdmin):
    list_display = ('cfs', 'bundle_ether', 'dko', 'sw', 'interface_sw', 'swb', 'interface_swb', 'pe', 'interface_pe', 'vrf', 'rd', 'unit', 'vt', 'sv', 'cv', 'bw', 'wan', 'wanv6', 'asn', 'lan', 'lbcpe', 'lnnid', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('cfs', 'bundle_ether', 'dko', 'sw', 'interface_sw', 'swb', 'interface_swb', 'pe', 'interface_pe', 'vrf', 'rd', 'unit', 'vt', 'sv', 'cv', 'bw', 'wan', 'wanv6', 'asn', 'lan', 'lbcpe', 'lnnid', 'created_at', 'updated_at')

admin.site.register(Datos, DatosAdmin)