from django.contrib import admin
from .models import Documentos

@admin.register(Documentos)
class DocumentosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_entrega','codigo_documentos','descripcion','fecha_emision','tiposervicio','tipo_documento']