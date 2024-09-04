from rest_framework import serializers
from apps.Valor.models  import Valor

class ValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valor
        fields = '__all__'
