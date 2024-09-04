from django.contrib import admin
from .models import Logos

@admin.register(Logos)
class LogosAdmin(admin.ModelAdmin):
    list_display = ['ruta', 'estado','nombre']
