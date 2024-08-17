from django.db import models

class Municipio(models.Model):
    nombre_municipio = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre_municipio