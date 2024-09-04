from django.db import models

class Variables(models.Model):

    class TipoDatoChoices(models.TextChoices):
        TEXT = 'text', 'Text'
        NUMBER = 'number', 'Number'
        DATE = 'date', 'Date'

    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)  
    tipo_dato = models.CharField(
        max_length=10,
        choices=TipoDatoChoices.choices,
        default=TipoDatoChoices.TEXT,
    )

    def __str__(self):
        return self.nombre

    def get_estado_display(self):
        return "Activo" if self.estado else "Inactivo"
