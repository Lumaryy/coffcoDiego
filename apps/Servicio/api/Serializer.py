from rest_framework import serializers
from apps.Servicio.models import Servicio

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '_all_'