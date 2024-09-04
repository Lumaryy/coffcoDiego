from django.db import models
from apps.Usuarios.models import Usuarios
from apps.Finca.models import Finca

class Muestra(models.Model):
    cantidad_entrada = models.DecimalField(max_digits=10, decimal_places=1)
    fecha_entrada = models.DateField()
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE)
    fecha_muestra = models.DateField()
    codigo_muestra = models.CharField(max_length=45)
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo_muestra
