from django.db import models

class Versiones(models.Model):
    version = models.CharField(max_length=45)
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    documentos = models.ForeignKey(Documentos, on_delete=models.CASCADE)
    estado = models.BooleanField()
    fecha_version = models.DateTimeField()

    def __str__(self):
        return self.version