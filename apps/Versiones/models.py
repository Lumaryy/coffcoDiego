from django.db import models
from apps.Usuarios.models import Usuarios
from apps.Documentos.models import Documentos
class Versiones(models.Model):
    version = models.CharField(max_length=45)
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    documentos = models.ForeignKey(Documentos, on_delete=models.CASCADE)
    estado = models.BooleanField()
    fecha_version = models.DateTimeField()

    def __str__(self):
        return self.version