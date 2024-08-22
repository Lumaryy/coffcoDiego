from rest_framework import viewsets
from apps.Finca.models import Finca
from apps.Finca.api.Serializer import FincaSerializer

class FincaViewSet(viewsets.ModelViewSet):
    queryset = Finca.objects.all()
    serializer_class = FincaSerializer