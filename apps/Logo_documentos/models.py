from django.db import models
from apps.Logos.models import Logos
from apps.Documentos.models import Documentos

class LogoDocumento(models.Model):
    logo_idlogos = models.ForeignKey( Logos, on_delete=models.CASCADE)
    documentos_iddocumentos = models.ForeignKey(Documentos, on_delete=models.CASCADE)

    def __str__(self):
        return self.logo_idlogos
