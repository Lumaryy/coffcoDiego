from django.db import models

class TipoDocumento(models.Model):
    nombreDocumento = models.CharField(max_length=45)
    estado = models.BooleanField(default=True)  

    def __str__(self):
        return self.nombreDocumento

    def get_estado_display(self):
        return "Activo" if self.estado else "Inactivo"
