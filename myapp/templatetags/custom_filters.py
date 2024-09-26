# myapp/templatetags/custom_filters.py
from django import template
import re

register = template.Library()

@register.filter
def extract_number(value):
    match = re.search(r'\d+', value)
    return match.group() if match else ''


@register.filter(name='strip')
def strip(value):
    return value.strip()