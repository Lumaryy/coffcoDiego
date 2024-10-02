from rest_framework import viewsets
from apps.Cambios.models import Cambios
from apps.Cambios.api.serializers import CambiosSerializer

class CambiosViewSet(viewsets.ModelViewSet):
    serializer_class = CambiosSerializer
    queryset = Cambios.objects.all()
