from rest_framework import viewsets
from apps.Documentos.models import  Documentos
from apps.Documentos.api.Serializer import DocumentosSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documentos.objects.all()
    serializer_class = DocumentosSerializer
