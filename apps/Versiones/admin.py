from django.contrib import admin
from .models import Versiones

@admin.register(Versiones)
class VersionesAdmin(admin.ModelAdmin):
    list_display = ['version','usuarios','documentos','estado','fecha_version']