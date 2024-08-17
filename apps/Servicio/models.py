from django.db import models
from apps.Ambiente.models import Ambiente
from apps.Muestra.models import Muestra
from apps.TipoServicio.models import Tiposervicio
from apps.Precio.models import Precio
from apps.Usuarios.models import Usuarios

class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=100)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    muestra = models.ForeignKey(Muestra, on_delete=models.CASCADE)
    fecha = models.DateField()
    tiposervicio = models.ForeignKey(Tiposervicio, on_delete=models.CASCADE)
    precio = models.ForeignKey(Precio, on_delete=models.CASCADE)
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre_servicio
