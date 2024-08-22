from rest_framework import viewsets
from apps.Usuarios.models import Usuarios
from apps.Usuarios.api.Serializer import  UsuariosSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer