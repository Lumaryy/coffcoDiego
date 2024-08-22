from rest_framework import serializers
from apps.Documentos.models import Documentos

class DocumentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentos
        fields = '_all_'
