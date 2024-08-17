from rest_framework import serializers
from models import *

class DocumentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentos
        fields = '_all_'
