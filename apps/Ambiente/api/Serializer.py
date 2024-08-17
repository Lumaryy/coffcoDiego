from rest_framework import serializers
from .models import *

class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = '_all_'