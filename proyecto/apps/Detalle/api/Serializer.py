from rest_framework import serializers
from apps.Detalle.models import Detalle

class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = '__all__'
