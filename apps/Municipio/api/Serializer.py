from rest_framework import serializers
from models import *

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '_all_'
