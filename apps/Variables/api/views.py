from rest_framework import viewsets
from apps.Variables.models import Variables
from apps.Variables.api.Serializer import VariablesSerializer

class VariableViewSet(viewsets.ModelViewSet):
    queryset = Variables.objects.all()
    serializer_class = VariablesSerializer