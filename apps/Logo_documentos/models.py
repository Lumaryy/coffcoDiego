from django.db import models

class LogoDocumento(models.Model):
    logo_idlogos = models.ForeignKey('Logo', on_delete=models.CASCADE)
    documentos_iddocumentos = models.ForeignKey('Documento', on_delete=models.CASCADE)

    def __str__(self):
        return self.logo_idlogos
