from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.Logo_documentos.models import LogoDocumento
from apps.Logo_documentos.api.Serializer import LogoDocumentoSerializer

class LogoDocumentoViewSet(viewsets.ViewSet):

    def list(self, request):
        logos = LogoDocumento.objects.all()
        serializer = LogoDocumentoSerializer(logos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            logo = LogoDocumento.objects.get(pk=pk)
        except LogoDocumento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LogoDocumentoSerializer(logo)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = LogoDocumentoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            logo = LogoDocumento.objects.get(pk=pk)
        except LogoDocumento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LogoDocumentoSerializer(logo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            logo = LogoDocumento.objects.get(pk=pk)
        except LogoDocumento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        logo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

