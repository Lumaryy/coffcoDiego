from django.contrib import admin
from .models import Variables

@admin.register(Variables)
class VariablesAdmin(admin.ModelAdmin):
    list_display = ['nombre','estado','tipo_dato']