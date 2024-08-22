from rest_framework import serializers
from apps.Variables.models import Variables

class VariablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variables
        fields = '_all_'
