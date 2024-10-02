from django.db import models
from apps.Documentos.models import Documentos

class Versiones(models.Model):
    
    version = models.CharField(max_length=45)
    documentos = models.ForeignKey(Documentos, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True) 
    nombre_documento = models.CharField(max_length=15)
    fecha_version = models.DateTimeField()

    def __str__(self):
        return self.version

    def get_estado_display(self):
        return "Activo" if self.estado else "Inactivo"
