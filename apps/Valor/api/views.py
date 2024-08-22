from rest_framework import viewsets
from apps.Valor.models import Valor
from apps.Valor.api.Serializer import  ValorSerializer

class ValorViewset(viewsets.ModelViewSet):
    queryset = Valor.objects.all()
    serializer_class = ValorSerializer