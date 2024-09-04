from django.contrib import admin
from .models import Servicio

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre','ambiente','muestra','fecha','tiposervicio','precio','usuarios','estado']