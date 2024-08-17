from django.db import models
from apps.TipoServicio.models import Tiposervicio

class Precio(models.Model):
    estado_precio = models.CharField(max_length=45)
    presentacion = models.CharField(max_length=45)
    precio = models.FloatField()
    tiposervicio = models.ForeignKey(Tiposervicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.estado_precio} - {self.presentacion}"
