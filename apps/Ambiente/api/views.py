from rest_framework import viewsets
from apps.Ambiente.models import Ambiente
from apps.Ambiente.api.Serializer import AmbienteSerializer

class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer