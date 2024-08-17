from rest_framework import viewsets
from models import Muestra
from Serializer import MuestraSerializer

class MuestraViewSet(viewsets.ModelViewSet):
    queryset = Muestra.objects.all()
    serializer_class = MuestraSerializer

