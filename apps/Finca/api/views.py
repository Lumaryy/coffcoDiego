from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.Finca.models import Finca
from apps.Finca.api.Serializer import FincaSerializer

class FincaViewSet(viewsets.ViewSet):

    def list(self, request):
        fincas = Finca.objects.all()
        serializer = FincaSerializer(fincas, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            finca = Finca.objects.get(pk=pk)
        except Finca.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FincaSerializer(finca)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = FincaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            finca = Finca.objects.get(pk=pk)
        except Finca.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FincaSerializer(finca, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            finca = Finca.objects.get(pk=pk)
        except Finca.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        finca.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
