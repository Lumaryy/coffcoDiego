from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.Rol.models import Rol
from apps.Rol.api.Serializer import RolSerializer

class RolViewSet(viewsets.ViewSet):

    def list(self, request):
        roles = Rol.objects.all()
        serializer = RolSerializer(roles, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            rol = Rol.objects.get(pk=pk)
        except Rol.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RolSerializer(rol)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = RolSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            rol = Rol.objects.get(pk=pk)
        except Rol.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RolSerializer(rol, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            rol = Rol.objects.get(pk=pk)
        except Rol.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rol.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
