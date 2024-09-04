from django.contrib import admin
from apps.Valor.models import Valor

@admin.register(Valor)
class ValorAdmin(admin.ModelAdmin):
    list_display = ['valor','servicio','detalle']
