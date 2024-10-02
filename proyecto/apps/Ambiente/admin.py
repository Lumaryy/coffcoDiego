from django.contrib import admin
from .models import Ambiente

@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    list_display = ['nombre_ambiente', 'estado']

