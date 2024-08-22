from rest_framework import viewsets
from apps.TipoServicio.models import Tiposervicio
from apps.TipoServicio.api.Serializer import TiposervicioSerializer

class TipoServicioViewSet(viewsets.ModelViewSet):
    queryset = Tiposervicio.objects.all()
    serializer_class = TiposervicioSerializer