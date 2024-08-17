from rest_framework import viewsets
from models import Ambiente
from Serializer import AmbienteSerializer

class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer