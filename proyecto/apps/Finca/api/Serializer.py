from rest_framework import serializers
from apps.Finca.models  import Finca

class FincaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finca
        fields = '_all_'