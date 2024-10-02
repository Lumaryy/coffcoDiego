from rest_framework import serializers
from apps.Versiones.models import Versiones

class VersionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Versiones
        fields = '_all_'