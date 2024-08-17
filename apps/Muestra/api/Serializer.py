from rest_framework import serializers
from models import *

class MuestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muestra
        fields = '_all_'