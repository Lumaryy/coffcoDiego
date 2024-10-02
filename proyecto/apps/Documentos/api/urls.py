from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Documentos.api.views import DocumentoViewSet

router_documentos = DefaultRouter()
router_documentos.register(prefix='documentos', basename='documentos', viewset=DocumentoViewSet)
