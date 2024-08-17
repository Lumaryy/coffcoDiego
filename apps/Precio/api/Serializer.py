from rest_framework import serializers
from models import *

class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = '_all_'