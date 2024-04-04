from django import template
from django.shortcuts import get_object_or_404

from ..models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu = get_object_or_404(Menu.objects.prefetch_related('sections'), name=menu_name)
    return {'sections': menu.sections.all()}
