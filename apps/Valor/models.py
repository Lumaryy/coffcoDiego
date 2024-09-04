from django.db import models
from apps.Servicio.models import Servicio
from apps.Detalle.models import Detalle


class Valor(models.Model):
    valor = models.CharField(max_length=45)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    detalle = models.ForeignKey(Detalle, on_delete=models.CASCADE)

    def __str__(self):
        return self.valor

