from django.db import models
from apps.Variables.models import Variables
from apps.Versiones.models import Versiones

class Detalle(models.Model):
    fk_idVariable = models.ForeignKey(Variables, on_delete=models.CASCADE)
    fk_id_version = models.ForeignKey(Versiones, on_delete=models.CASCADE)

    def __str__(self):
        return self.fk_id_variable
