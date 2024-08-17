from rest_framework import viewsets
from models import TipoDocumento
from Serializer import TipoDocumentoSerializer

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer