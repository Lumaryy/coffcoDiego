from django.db import models

class Logos(models.Model):
    ruta = models.CharField(max_length=150)
    estado = models.BooleanField(default=True) 
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.ruta})"

    def get_estado_display(self):
        return "Activo" if self.estado else "Inactivo"
