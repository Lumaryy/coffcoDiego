from rest_framework import viewsets
from models import  Precio
from Serializer import PrecioSerializer

class PrecioViewSet(viewsets.ModelViewSet):
    queryset = Precio.objects.all()
    serializer_class = PrecioSerializer