from django.db import models
from apps.Ambiente.models import Ambiente
from apps.Muestra.models import Muestra
from apps.TipoServicio.models import Tiposervicio
from apps.Precio.models import Precio
from apps.Usuarios.models import Usuarios

class Servicio(models.Model):
    EN_PROCESO = 'en proceso'
    TERMINADO = 'terminado'

    ESTADO_CHOICES = [
        (EN_PROCESO, 'En Proceso'),
        (TERMINADO, 'Terminado'),
    ]

    tiposervicio = models.ForeignKey(Tiposervicio, on_delete=models.CASCADE)
    fecha = models.DateField()
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    muestra = models.ForeignKey(Muestra, on_delete=models.CASCADE)
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    cantidad_salida = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(
        max_length=11, 
        choices=ESTADO_CHOICES, 
        default=EN_PROCESO
    )

    def __str__(self):
        return f"{self.tiposervicio} - {self.fecha}"

