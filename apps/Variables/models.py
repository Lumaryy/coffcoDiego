from django.db import models

class Variables(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField()
    versiones = models.ForeignKey(Versiones, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre