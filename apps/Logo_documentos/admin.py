from django.contrib import admin
from .models import LogoDocumento

@admin.register(LogoDocumento)
class LogoDocumentoAdmin(admin.ModelAdmin):
    list_display = ['logo_idlogos', 'documentos_iddocumentos']



