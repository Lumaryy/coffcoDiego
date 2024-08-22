from rest_framework import viewsets
from apps.Municipio.models import Municipio
from apps.Municipio.api.Serializer import MunicipioSerializer

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
