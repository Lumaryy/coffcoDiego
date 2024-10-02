from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.Servicio.models import Servicio
from apps.Servicio.api.Serializer import ServicioSerializer

class ServicioViewSet(viewsets.ViewSet):

    def list(self, request):
        servicios = Servicio.objects.all()
        serializer = ServicioSerializer(servicios, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            servicio = Servicio.objects.get(pk=pk)
        except Servicio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ServicioSerializer(servicio)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            servicio = Servicio.objects.get(pk=pk)
        except Servicio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ServicioSerializer(servicio, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            servicio = Servicio.objects.get(pk=pk)
        except Servicio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        servicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
