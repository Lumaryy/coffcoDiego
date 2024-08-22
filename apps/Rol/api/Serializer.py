from rest_framework import serializers
from apps.Rol.models import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '_all_'
