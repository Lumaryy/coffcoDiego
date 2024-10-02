from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.Usuarios.models import Usuarios
from apps.Usuarios.api.Serializer import UsuariosSerializer

class UsuarioViewSet(viewsets.ViewSet):

    def list(self, request):
        usuarios = Usuarios.objects.all()
        serializer = UsuariosSerializer(usuarios, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            usuario = Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UsuariosSerializer(usuario)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            usuario = Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UsuariosSerializer(usuario, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            usuario = Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
