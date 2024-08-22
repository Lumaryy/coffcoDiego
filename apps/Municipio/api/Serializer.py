from rest_framework import serializers
from apps.Municipio.models import Municipio

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '_all_'
