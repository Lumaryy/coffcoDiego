from django.db import models
from apps.Usuarios.models import Usuarios
from apps.Finca.models import Finca
from apps.TipoServicio.models import Tiposervicio

class Muestra(models.Model):
    PENDIENTE = 'pendiente'
    TERMINADO = 'terminado'
    
    ESTADO_CHOICES = [
        (PENDIENTE, 'Pendiente'),
        (TERMINADO, 'Terminado'),
    ]

    cantidad_entrada = models.DecimalField(max_digits=10, decimal_places=1)
    fecha_entrada = models.DateField()
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE)
    fecha_muestra = models.DateField()
    codigo_muestra = models.CharField(max_length=45)
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    estado = models.CharField(
        max_length=9, 
        choices=ESTADO_CHOICES, 
        default=PENDIENTE
    )
    altura = models.DecimalField(max_digits=10, decimal_places=2)
    variedad = models.CharField(max_length=45)
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    fk_idTipoServicio = models.ForeignKey(Tiposervicio, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo_muestra
