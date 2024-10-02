from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.Versiones.models import Versiones
from apps.Versiones.api.Serializer import VersionesSerializer

class VersionViewSet(viewsets.ViewSet):
    
    def list(self, request):
        versiones = Versiones.objects.all()
        serializer = VersionesSerializer(versiones, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            version = Versiones.objects.get(pk=pk)
        except Versiones.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VersionesSerializer(version)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = VersionesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            version = Versiones.objects.get(pk=pk)
        except Versiones.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VersionesSerializer(version, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            version = Versiones.objects.get(pk=pk)
        except Versiones.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        version.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
