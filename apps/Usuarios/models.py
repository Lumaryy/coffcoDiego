from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from apps.Rol.models import Rol

class UsuariosManager(BaseUserManager):
    def create_user(self, correo_electronico, contrasena=None, **extra_fields):
        if not correo_electronico:
            raise ValueError("El correo electrónico es obligatorio")
        usuario = self.model(correo_electronico=correo_electronico, **extra_fields)
        usuario.set_password(contrasena)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo_electronico, contrasena=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(correo_electronico, contrasena, **extra_fields)

class Usuarios(AbstractBaseUser, PermissionsMixin):
    class TipoDocumentoChoices(models.TextChoices):
        CC = 'cc', 'Cédula de Ciudadanía'
        TI = 'ti', 'Tarjeta de Identidad'
        NIT = 'nit', 'NIT'
        PASAPORTE = 'pasaporte', 'Pasaporte'

    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    correo_electronico = models.EmailField(max_length=100, unique=True)
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

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre', 'apellidos', 'telefono', 'tipo_documento', 'numero_documento', 'rol']

    objects = UsuariosManager()

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

    def get_estado_display(self):
        return "Activo" if self.estado else "Inactivo"
