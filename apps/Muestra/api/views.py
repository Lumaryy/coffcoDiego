from rest_framework import viewsets
from apps.Muestra.models import Muestra
from apps.Muestra.api.Serializer import MuestraSerializer

class MuestraViewSet(viewsets.ModelViewSet):
    queryset = Muestra.objects.all()
    serializer_class = MuestraSerializer

