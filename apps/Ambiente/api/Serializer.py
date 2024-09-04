from rest_framework import serializers
from apps.Ambiente.models import Ambiente

class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = '__all__'



