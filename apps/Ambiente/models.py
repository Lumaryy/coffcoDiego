from django.db import models

class Ambiente(models.Model):
    nombre_ambiente = models.CharField(max_length=45)
    estado = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.nombre_ambiente

    def get_estado_display(self):
        return "Activo" if self.estado else "Inactivo"

