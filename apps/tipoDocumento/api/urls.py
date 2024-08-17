from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TipoDocumentoViewSet

router = DefaultRouter()

router.register(r'tipo_documento', TipoDocumentoViewSet)

