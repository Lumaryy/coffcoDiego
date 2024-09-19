from rest_framework import serializers
from apps.Ambiente.models import Ambiente

class AmbienteSerializer(serializers.ModelSerializer):
    estado_display = serializers.SerializerMethodField()

    class Meta:
        model = Ambiente
        fields = ['id', 'nombre_ambiente', 'estado', 'estado_display']

    def get_estado_display(self, obj):
        return obj.get_estado_display()
