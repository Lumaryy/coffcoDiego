from rest_framework import viewsets
from models import Finca
from Serializer import FincaSerializer

class FincaViewSet(viewsets.ModelViewSet):
    queryset = Finca.objects.all()
    serializer_class = FincaSerializer