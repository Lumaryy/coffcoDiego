from rest_framework import viewsets
from models import Tiposervicio
from Serializer import TiposervicioSerializer

class TipoServicioViewSet(viewsets.ModelViewSet):
    queryset = Tiposervicio.objects.all()
    serializer_class = TiposervicioSerializer