import markdown as md
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="markdown")
def markdown_filter(value):
    return mark_safe(md.markdown(value or "", extensions=["fenced_code", "codehilite", "tables"]))
