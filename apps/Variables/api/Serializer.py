from rest_framework import serializers
from models import *

class VariablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variables
        fields = '_all_'
