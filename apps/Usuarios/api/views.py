from rest_framework import viewsets
from models import Usuarios
from Serializer import  UsuariosSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer