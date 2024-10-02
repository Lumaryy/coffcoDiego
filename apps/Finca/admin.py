from django.contrib import admin
from .models import Finca


@admin.register(Finca)
class FincaAdmin(admin.ModelAdmin):
    list_display = ['nombre_finca', 'municipio']
