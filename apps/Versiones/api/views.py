from rest_framework import viewsets
from models import Versiones
from Serializer import VersionesSerializer

class VersionViewSet(viewsets.ModelViewSet):
    queryset = Versiones.objects.all()
    serializer_class = VersionesSerializer