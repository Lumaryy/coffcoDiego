from rest_framework import serializers
from apps.TipoServicio.models import Tiposervicio

class TiposervicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiposervicio
        fields = '_all_'