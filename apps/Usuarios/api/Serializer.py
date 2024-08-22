from rest_framework import serializers
from apps.Usuarios.models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '_all_'
