from rest_framework import serializers
from apps.Precio.models import Precio

class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = '_all_'