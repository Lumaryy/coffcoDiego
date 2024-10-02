from django.db import models
from apps.TipoServicio.models import Tiposervicio
from apps.tipoDocumento.models import TipoDocumento

class Documentos(models.Model):
    ENTRADA = 'entrada'
    SALIDA = 'salida'

    ENTRADA_SALIDA_CHOICES = [
        (ENTRADA, 'Entrada'),
        (SALIDA, 'Salida'),
    ]

    nombre = models.CharField(max_length=100)
    fecha_carga = models.DateField()
    codigo_documentos = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha_emision = models.DateField()
    tiposervicio = models.ForeignKey(Tiposervicio, on_delete=models.CASCADE)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    entrada_salida = models.CharField(
        max_length=7,
        choices=ENTRADA_SALIDA_CHOICES,
        default=ENTRADA,
    )

    def __str__(self):
        return self.nombre
