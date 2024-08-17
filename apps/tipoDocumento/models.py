from django.db import models

class TipoDocumento(models.Model):
    nombreDocumento = models.CharField(max_length=45)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombreDocumento


