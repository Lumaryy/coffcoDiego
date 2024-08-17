from rest_framework import serializers
from models import *

class LogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logos
        fields = '_all_'