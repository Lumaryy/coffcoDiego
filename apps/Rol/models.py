from django.db import models

class Rol(models.Model):
    rol = models.CharField(max_length=100)

    def __str__(self):
        return self.rol
