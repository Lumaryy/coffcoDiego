from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.Municipio.models import Municipio
from apps.Municipio.api.Serializer import MunicipioSerializer

class MunicipioViewSet(viewsets.ViewSet):

    def list(self, request):
        municipios = Municipio.objects.all()
        serializer = MunicipioSerializer(municipios, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MunicipioSerializer(municipio)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = MunicipioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MunicipioSerializer(municipio, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        municipio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
