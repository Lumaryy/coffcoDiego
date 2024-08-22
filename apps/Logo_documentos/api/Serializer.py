from rest_framework import serializers
from apps.Logo_documentos.models import LogoDocumento

class LogoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogoDocumento
        fields = '_all_'
