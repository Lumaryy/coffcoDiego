from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.TipoServicio.models import Tiposervicio
from apps.TipoServicio.api.Serializer import TiposervicioSerializer

class TipoServicioViewSet(viewsets.ViewSet):

    def list(self, request):
        tipos_servicio = Tiposervicio.objects.all()
        serializer = TiposervicioSerializer(tipos_servicio, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            tiposervicio = Tiposervicio.objects.get(pk=pk)
        except Tiposervicio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TiposervicioSerializer(tiposervicio)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = TiposervicioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            tiposervicio = Tiposervicio.objects.get(pk=pk)
        except Tiposervicio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TiposervicioSerializer(tiposervicio, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            tiposervicio = Tiposervicio.objects.get(pk=pk)
        except Tiposervicio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        tiposervicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
