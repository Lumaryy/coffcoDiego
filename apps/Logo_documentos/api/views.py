from rest_framework import viewsets
from apps.Logo_documentos.models import  LogoDocumento
from apps.Logo_documentos.api.Serializer import LogoDocumentoSerializer

class LogoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = LogoDocumento.objects.all()
    serializer_class = LogoDocumentoSerializer
