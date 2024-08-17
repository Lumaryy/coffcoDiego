from django.db import models
from apps.Usuarios.models import Usuarios

class Muestra(models.Model):
    cantidad_entrada = models.FloatField()
    fecha_entrada = models.DateField()
    fecha_muestra = models.DateField()
    codigo_muestra = models.CharField(max_length=45)
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo_muestra
