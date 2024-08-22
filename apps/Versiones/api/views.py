from rest_framework import viewsets
from apps.Versiones.models import Versiones
from apps.Versiones.api.Serializer import VersionesSerializer

class VersionViewSet(viewsets.ModelViewSet):
    queryset = Versiones.objects.all()
    serializer_class = VersionesSerializer