# myapp/templatetags/network_filters.py
from django import template
import ipaddress

register = template.Library()

@register.filter
def first_valid_ip_with_mask(network):
    net = ipaddress.IPv4Network(network, strict=False)
    first_valid_ip = net.network_address + 1
    return f"{first_valid_ip}/{net.prefixlen}"

@register.filter
def first_valid_ip(network):
    net = ipaddress.IPv4Network(network, strict=False)
    first_valid_ip = net.network_address + 1
    return str(first_valid_ip)

@register.filter
def second_valid_ip(network):
    net = ipaddress.IPv4Network(network, strict=False)
    second_valid_ip = net.network_address + 2
    return str(second_valid_ip)


@register.filter
def first_valid_ipv6_with_mask(network):
    net = ipaddress.IPv6Network(network, strict=False)
    first_valid_ip = net.network_address + 1
    return f"{first_valid_ip}/{net.prefixlen}"

@register.filter
def first_valid_ipv6(network):
    net = ipaddress.IPv6Network(network, strict=False)
    first_valid_ip = net.network_address + 1
    return str(first_valid_ip)

@register.filter
def second_valid_ipv6(network):
    net = ipaddress.IPv6Network(network, strict=False)
    second_valid_ip = net.network_address + 2
    return str(second_valid_ip)