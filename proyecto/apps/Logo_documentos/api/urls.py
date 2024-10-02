from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Logo_documentos.api.views import LogoDocumentoViewSet

router_logoDocumentos = DefaultRouter()

router_logoDocumentos.register(prefix='logoDocumentos', basename='logoDocumentos', viewset=LogoDocumentoViewSet)
