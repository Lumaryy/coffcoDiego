from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.Rol.models import Rol
from apps.Rol.api.Serializer import RolSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

    def list(self, request):
        roles = self.get_queryset()
        serializer = self.get_serializer(roles, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk=None):
        try:
            rol = self.get_object()
        except Rol.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(rol)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
