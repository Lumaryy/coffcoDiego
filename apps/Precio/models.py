from django.db import models
from apps.TipoServicio.models import Tiposervicio

class Precio(models.Model):
    LB = 'Lb'
    KG = 'Kg'

    UNIDAD_MEDIDA_CHOICES = [
        (LB, 'Libra'),
        (KG, 'Kilogramo'),
    ]

    estado_precio = models.BooleanField(default=True)
    presentacion = models.CharField(max_length=45)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    tiposervicio = models.ForeignKey(Tiposervicio, on_delete=models.CASCADE)
    unidad_medida = models.CharField(
        max_length=2,
        choices=UNIDAD_MEDIDA_CHOICES,
        default=LB,
    )

    def __str__(self):
        return f"{self.presentacion} - {self.precio} - {self.tiposervicio} - {self.unidad_medida}"

    def get_estado_precio_display(self):
        return "Activo" if self.estado_precio else "Inactivo"
