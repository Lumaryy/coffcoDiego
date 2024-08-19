from django.db import models
from apps.TipoServicio.models import Tiposervicio
from apps.tipoDocumento.models import TipoDocumento
from apps.Logos.models import Logos


class Documentos(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    codigo_documentos = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha_fimision = models.DateField()
    tiposervicio = models.ForeignKey(Tiposervicio, on_delete=models.CASCADE)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    logos = models.ForeignKey(Logos, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
