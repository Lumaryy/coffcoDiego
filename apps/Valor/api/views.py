from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.Valor.models import Valor
from apps.Valor.api.Serializer import ValorSerializer
#from rest_framework.permissons import IsAuthenticated, IsAdminUser

class ValorViewSet(viewsets.ViewSet):

    def list(self, request):
        valores = Valor.objects.all()
        serializer = ValorSerializer(valores, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            valor = Valor.objects.get(pk=pk)
        except Valor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ValorSerializer(valor)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = ValorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            valor = Valor.objects.get(pk=pk)
        except Valor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ValorSerializer(valor, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            valor = Valor.objects.get(pk=pk)
        except Valor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        valor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
