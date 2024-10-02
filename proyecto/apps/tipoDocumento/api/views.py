from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.tipoDocumento.models import TipoDocumento
from apps.tipoDocumento.api.Serializer import TipoDocumentoSerializer

class TipoDocumentoViewSet(viewsets.ViewSet):

    def list(self, request):
        tipos_documento = TipoDocumento.objects.all()
        serializer = TipoDocumentoSerializer(tipos_documento, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            tipo_documento = TipoDocumento.objects.get(pk=pk)
        except TipoDocumento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TipoDocumentoSerializer(tipo_documento)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = TipoDocumentoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            tipo_documento = TipoDocumento.objects.get(pk=pk)
        except TipoDocumento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TipoDocumentoSerializer(tipo_documento, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            tipo_documento = TipoDocumento.objects.get(pk=pk)
        except TipoDocumento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        tipo_documento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
