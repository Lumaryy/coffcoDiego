from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.Documentos.models import Documentos
from apps.Documentos.api.Serializer import DocumentosSerializer

class DocumentoViewSet(viewsets.ViewSet):

    def list(self, request):
        documentos = Documentos.objects.all()
        serializer = DocumentosSerializer(documentos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            documento = Documentos.objects.get(pk=pk)
        except Documentos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DocumentosSerializer(documento)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = DocumentosSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            documento = Documentos.objects.get(pk=pk)
        except Documentos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DocumentosSerializer(documento, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            documento = Documentos.objects.get(pk=pk)
        except Documentos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        documento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
