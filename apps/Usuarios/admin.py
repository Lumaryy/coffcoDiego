from django.contrib import admin
from .models import Usuarios

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    # Define los campos que se mostrarán en el formulario de administración
    fieldsets = (
        (None, {
            'fields': ('nombre', 'apellidos', 'correo_electronico', 'telefono', 'tipo_documento', 'numero_documento', 'estado', 'rol')
        }),
        ('Contraseña', {
            'fields': ('contrasena',)  # Manejo de contraseñas (considera la seguridad)
        }),
    )

    # Define los campos que se mostrarán en la lista del panel de administración
    list_display = ('nombre', 'apellidos', 'correo_electronico', 'telefono', 'tipo_documento', 'get_estado_display', 'rol')
    
    # Define el orden por defecto
    ordering = ('nombre',)  # Cambia esto a un campo existente en Usuarios

    # Opcional: Puedes añadir filtros en el panel de administración
    list_filter = ('estado', 'tipo_documento', 'rol')
    
    # Opcional: Puedes añadir un campo de búsqueda
    search_fields = ('nombre', 'apellidos', 'correo_electronico')

