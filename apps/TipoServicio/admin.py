from django.contrib import admin
from .models import Tiposervicio


@admin.register(Tiposervicio)
class TiposervicioAdmin(admin.ModelAdmin):
    list_display = ['codigoTipoServicio','nombreServicio','estado']