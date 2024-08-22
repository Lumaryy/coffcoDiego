from rest_framework import viewsets
from apps.Detalle.models import Detalle
from apps.Detalle.api.Serializer import DetalleSerializer

class DetalleViewSet(viewsets.ModelViewSet):
    queryset = Detalle.objects.all()
    serializer_class = DetalleSerializer
