from rest_framework import serializers
from apps.tipoDocumento.models import TipoDocumento

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '_all_'