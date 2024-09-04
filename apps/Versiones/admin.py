from django.contrib import admin
from .models import Versiones

@admin.register(Versiones)
class VersionesAdmin(admin.ModelAdmin):
    list_display = ['version','documentos','estado','nombre_documento','fecha_version']