from rest_framework import serializers
from models import *

class TiposervicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiposervicio
        fields = '_all_'