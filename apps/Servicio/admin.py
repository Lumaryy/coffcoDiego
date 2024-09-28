from django.contrib import admin
from .models import Servicio

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = [
        'tiposervicio', 
        'ambiente', 
        'muestra', 
        'fecha', 
        'fecha_fin', 
        'usuarios', 
        'cantidad_salida', 
        'estado'
    ]
