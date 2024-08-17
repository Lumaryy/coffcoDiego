from rest_framework import viewsets
from models import  Documentos
from Serializer import DocumentosSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documentos.objects.all()
    serializer_class = DocumentosSerializer
