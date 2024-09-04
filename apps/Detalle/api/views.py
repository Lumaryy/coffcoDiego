from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.Detalle.models import Detalle
from apps.Detalle.api.Serializer import DetalleSerializer

class DetalleViewSet(viewsets.ViewSet):

    def list(self, request):
        detalles = Detalle.objects.all()
        serializer = DetalleSerializer(detalles, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            detalle = Detalle.objects.get(pk=pk)
        except Detalle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DetalleSerializer(detalle)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = DetalleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            detalle = Detalle.objects.get(pk=pk)
        except Detalle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DetalleSerializer(detalle, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def delete(self, request, pk=None):
        try:
            detalle = Detalle.objects.get(pk=pk)
        except Detalle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        detalle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
