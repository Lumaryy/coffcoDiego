from django.db import models

class Tiposervicio(models.Model):
    codigoTipoServicio = models.CharField(max_length=45)
    nombreServicio = models.CharField(max_length=45)
    estado = models.BooleanField(default=True)  

    def __str__(self):
        return self.codigoTipoServicio

    def get_estado_display(self):
        return "Activo" if self.estado else "Inactivo"