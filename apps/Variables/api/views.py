from rest_framework import viewsets
from models import Variables
from Serializer import VariablesSerializer

class VariableViewSet(viewsets.ModelViewSet):
    queryset = Variables.objects.all()
    serializer_class = VariablesSerializer