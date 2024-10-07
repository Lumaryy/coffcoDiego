from rest_framework import serializers
from apps.Usuarios.models import Usuarios
from apps.Rol.api.Serializer import RolSerializer  # Importamos el serializador del Rol

class UsuariosGetSerializer(serializers.ModelSerializer):
    rol = RolSerializer()  # Esto mostrará la información completa del rol, no solo el ID
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)  # Mostrará "Activo" o "Inactivo"

    class Meta:
        model = Usuarios
        fields = ['id', 'nombre', 'apellidos', 'correo_electronico', 'telefono', 'tipo_documento', 'numero_documento', 'estado_display', 'rol']

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellidos', 'correo_electronico', 'telefono', 'tipo_documento', 'numero_documento', 'estado', 'rol']

class UsuariosUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellidos', 'correo_electronico', 'telefono', 'tipo_documento', 'numero_documento', 'estado', 'rol']
