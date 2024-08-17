from rest_framework import serializers
from models import *

class FincaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finca
        fields = '_all_'