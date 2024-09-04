from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.Muestra.models import Muestra
from apps.Muestra.api.Serializer import MuestraSerializer

class MuestraViewSet(viewsets.ViewSet):

    def list(self, request):
        muestras = Muestra.objects.all()
        serializer = MuestraSerializer(muestras, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            muestra = Muestra.objects.get(pk=pk)
        except Muestra.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MuestraSerializer(muestra)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = MuestraSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            muestra = Muestra.objects.get(pk=pk)
        except Muestra.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MuestraSerializer(muestra, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            muestra = Muestra.objects.get(pk=pk)
        except Muestra.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        muestra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
