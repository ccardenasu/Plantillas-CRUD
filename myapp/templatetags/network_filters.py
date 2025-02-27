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
def second_valid_ip_with_mask(network):
    net = ipaddress.IPv4Network(network, strict=False)
    second_valid_ip = net.network_address + 2
    return f"{second_valid_ip}/{net.prefixlen}"

@register.filter
def first_ip_no_mask(network):
    net = ipaddress.IPv4Network(network, strict=False)
    first_valid_ip = net.network_address
    return f"{first_valid_ip}"

@register.filter
def mask(network):
    net = ipaddress.IPv4Network(network, strict=False)
    return f"{net.prefixlen}"

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
def maskv6(network):
    net = ipaddress.IPv6Network(network, strict=False)
    return f"{net.prefixlen}"

@register.filter
def first_ipv6_no_mask(network):
    net = ipaddress.IPv6Network(network, strict=False)
    first_valid_ip = net.network_address
    return f"{first_valid_ip}"

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

@register.filter
def calculate_previous_ip_filter(ip_without_prefix):
    return calculate_previous_ip(ip_without_prefix)

def calculate_previous_ip(ip_without_prefix):
    ip = ipaddress.ip_address(ip_without_prefix)
    new_ip = ip - 1
    new_ip_with_prefix = f"{new_ip}/31"    
    return new_ip_with_prefix

@register.filter
def calculate_previous_ip_no_mask_filter(ip_without_prefix):
    return calculate_previous_ip_no_mask(ip_without_prefix)

def calculate_previous_ip_no_mask(ip_without_prefix):
    ip = ipaddress.ip_address(ip_without_prefix)
    new_ip = ip - 1
    new_ip_with_no_mask_prefix = f"{new_ip}"    
    return new_ip_with_no_mask_prefix
