from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.Ambiente.models import Ambiente
from apps.Ambiente.api.Serializer import AmbienteSerializer

class AmbienteViewSet(viewsets.ViewSet):

    def list(self, request):
        ambientes = Ambiente.objects.all()
        serializer = AmbienteSerializer(ambientes, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            ambiente = Ambiente.objects.get(pk=pk)
        except Ambiente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AmbienteSerializer(ambiente)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = AmbienteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            ambiente = Ambiente.objects.get(pk=pk)
        except Ambiente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AmbienteSerializer(ambiente, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            ambiente = Ambiente.objects.get(pk=pk)
        except Ambiente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ambiente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
