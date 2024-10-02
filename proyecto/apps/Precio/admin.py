from django.contrib import admin
from .models import Precio

@admin.register(Precio)
class PrecioAdmin(admin.ModelAdmin):
    list_display = ['estado_precio', 'presentacion','precio','tiposervicio','unidad_medida']
