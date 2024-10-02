from rest_framework import serializers
from apps.Cambios.models import Cambios

class CambiosSerializer(serializers.ModelSerializer):
    estado_cambio_display = serializers.SerializerMethodField()

    class Meta:
        model = Cambios
        fields = ['id', 'descripcion', 'fecha', 'servicio', 'usuario', 'estado_cambio', 'estado_cambio_display']

    def get_estado_cambio_display(self, obj):
        return obj.get_estado_cambio_display()  
