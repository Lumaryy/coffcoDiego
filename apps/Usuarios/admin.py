from django.contrib import admin
from .models import Usuarios

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellidos','correo_electronico','contrasena','tipo_documento','numero_documento','estado','rol']

