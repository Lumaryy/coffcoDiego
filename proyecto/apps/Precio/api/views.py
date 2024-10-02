from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.Precio.models import Precio
from apps.Precio.api.Serializer import PrecioSerializer

class PrecioViewSet(viewsets.ViewSet):

    def list(self, request):
        precios = Precio.objects.all()
        serializer = PrecioSerializer(precios, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            precio = Precio.objects.get(pk=pk)
        except Precio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PrecioSerializer(precio)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = PrecioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            precio = Precio.objects.get(pk=pk)
        except Precio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PrecioSerializer(precio, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            precio = Precio.objects.get(pk=pk)
        except Precio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        precio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
