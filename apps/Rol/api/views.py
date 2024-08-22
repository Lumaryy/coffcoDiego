from rest_framework import viewsets
from apps.Rol.models import Rol
from apps.Rol.api.Serializer import RolSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
