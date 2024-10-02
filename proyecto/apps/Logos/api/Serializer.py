from rest_framework import serializers
from apps.Logos.models import Logos

class LogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logos
        fields = '_all_'