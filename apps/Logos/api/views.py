from rest_framework import viewsets
from apps.Logos.models import Logos
from apps.Logos.api.Serializer import LogosSerializer 

class LogoViewSet(viewsets.ModelViewSet):
    queryset = Logos.objects.all()
    serializer_class = LogosSerializer
    