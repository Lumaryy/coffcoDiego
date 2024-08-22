from rest_framework import viewsets
from apps.tipoDocumento.models import TipoDocumento
from apps.tipoDocumento.api.Serializer import TipoDocumentoSerializer

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer