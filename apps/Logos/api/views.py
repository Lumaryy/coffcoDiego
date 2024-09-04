from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.Logos.models import Logos
from apps.Logos.api.Serializer import LogosSerializer

class LogoViewSet(viewsets.ViewSet):

    def list(self, request):
        logos = Logos.objects.all()
        serializer = LogosSerializer(logos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            logo = Logos.objects.get(pk=pk)
        except Logos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LogosSerializer(logo)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        serializer = LogosSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, pk=None):
        try:
            logo = Logos.objects.get(pk=pk)
        except Logos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LogosSerializer(logo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def destroy(self, request, pk=None):
        try:
            logo = Logos.objects.get(pk=pk)
        except Logos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        logo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
