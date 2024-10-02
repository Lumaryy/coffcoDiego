from django.db import models
from apps.Rol.models import Rol

class Usuarios(models.Model):

    class TipoDocumentoChoices(models.TextChoices):
        CC = 'cc', 'Cédula de Ciudadanía'
        TI = 'ti', 'Tarjeta de Identidad'
        NIT = 'nit', 'NIT'
        PASAPORTE = 'pasaporte', 'Pasaporte'

    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    correo_electronico = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=128)
    tipo_documento = models.CharField(
        max_length=10,
        choices=TipoDocumentoChoices.choices,
        default=TipoDocumentoChoices.CC,
    )
    numero_documento = models.CharField(max_length=20)
    estado = models.BooleanField(default=True) 
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

    def get_estado_display(self):
        return "Activo" if self.estado else "Inactivo"
