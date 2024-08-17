from rest_framework import viewsets
from models import Servicio
from Serializer import ServicioSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
