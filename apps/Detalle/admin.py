from django.contrib import admin
from .models import Detalle

@admin.register(Detalle)
class DetalleAdmin(admin.ModelAdmin):
    list_display = ('fk_idVariable', 'fk_id_version')
