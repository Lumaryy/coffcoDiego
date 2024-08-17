from django.db import models
from apps.tipoDocumento.models import TipoDocumento
from apps.Rol.models import Rol

class Usuarios(models.Model):
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    correo_electronico = models.EmailField(max_length=100)
    contrasena = models.CharField(max_length=45)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento = models.IntegerField()
    estado = models.BooleanField()
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
