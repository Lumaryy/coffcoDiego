from rest_framework import viewsets
from apps.Servicio.models import Servicio
from apps.Servicio.api.Serializer import ServicioSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
