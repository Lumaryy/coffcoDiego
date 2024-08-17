from rest_framework import viewsets
from models import Logos
from Serializer import LogosSerializer 

class LogoViewSet(viewsets.ModelViewSet):
    queryset = Logos.objects.all()
    serializer_class = LogosSerializer
    