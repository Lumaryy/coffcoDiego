from django.db import models

class Logos(models.Model):
    logo = models.CharField(max_length=45)
    estado = models.BooleanField()

    def __str__(self):
        return self.logo
