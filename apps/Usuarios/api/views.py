from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.Usuarios.models import Usuarios
from apps.Usuarios.api.Serializer import UsuariosSerializer, UsuariosUpdateSerializer, UsuariosGetSerializer

class UsuarioViewSet(viewsets.ViewSet):

    def list(self, request):
        usuarios = Usuarios.objects.all()
        serializer = UsuariosGetSerializer(usuarios, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            usuario = Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UsuariosGetSerializer(usuario)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_data = {
                "message": "Usuario registrado exitosamente",
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            usuario = Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UsuariosUpdateSerializer(usuario, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            usuario = Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


