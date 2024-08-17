from django.db import models

class Tiposervicio(models.Model):
    nombreServicio = models.CharField(max_length=45)

    def __str__(self):
        return self.nombreServicio
