from django.contrib import admin
from .models import Muestra

@admin.register(Muestra)
class MuestraAdmin(admin.ModelAdmin):
    list_display = [
        'cantidad_entrada', 
        'fecha_entrada', 
        'finca', 
        'fecha_muestra', 
        'codigo_muestra', 
        'usuarios', 
        'estado', 
        'altura', 
        'variedad', 
        'observaciones', 
        'fk_idTipoServicio'
    ]
