from django.contrib import admin
from .models import Valor

@admin.register(Valor)
class ValorAdmin(admin.ModelAdmin):
    list_display = ['valor','servicio','variables']
