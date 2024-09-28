from django.db import models

class Cambios(models.Model):
    PENDIENTE = 'pendiente'
    APROBADO = 'aprobado'
    DESAPROBADO = 'desaprobado'
    
    ESTADO_CAMBIO_CHOICES = [
        (PENDIENTE, 'Pendiente'),
        (APROBADO, 'Aprobado'),
        (DESAPROBADO, 'Desaprobado'),
    ]
    
    descripcion = models.TextField()
    fecha = models.DateField()
    fk_id_servicio = models.IntegerField() 
    fk_id_usuario = models.IntegerField()  
    estado_cambio = models.CharField(
        max_length=11,
        choices=ESTADO_CAMBIO_CHOICES,
        default=PENDIENTE,
    )

    def __str__(self):
        return f"Cambio {self.id} - {self.descripcion[:30]}..."

    def get_estado_cambio_display(self):
        return dict(self.ESTADO_CAMBIO_CHOICES).get(self.estado_cambio, 'Desconocido')
