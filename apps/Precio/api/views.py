from rest_framework import viewsets
from apps.Precio.models import  Precio
from apps.Precio.api.Serializer import PrecioSerializer

class PrecioViewSet(viewsets.ModelViewSet):
    queryset = Precio.objects.all()
    serializer_class = PrecioSerializer