# myapp/templatetags/network_filters.py
from django import template
import ipaddress

register = template.Library()

@register.filter
def first_valid_ip_with_mask(network):
    net = ipaddress.IPv4Network(network, strict=False)
    first_valid_ip = net.network_address + 1
    return f"{first_valid_ip}/{net.prefixlen}"
