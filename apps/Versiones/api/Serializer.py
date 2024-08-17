from rest_framework import serializers
from models import *

class VersionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Versiones
        fields = '_all_'