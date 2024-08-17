from django.db import models
from apps.Municipio.models import Municipio
class Finca(models.Model):
    nombre_finca = models.CharField(max_length=50)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_finca