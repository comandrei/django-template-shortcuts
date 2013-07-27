from django import template
from jquery import jquery

register = template.Library()

register.tag("jquery", jquery)
