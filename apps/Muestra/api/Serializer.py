from rest_framework import serializers
from apps.Muestra.models import Muestra

class MuestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muestra
        fields = '_all_'