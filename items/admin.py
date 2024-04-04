from django.contrib import admin
from .models import Section, Menu


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass
