from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Valor.api.views import ValorViewSet 

router_valor = DefaultRouter()
router_valor.register(prefix='valor', basename='valor', viewset=ValorViewSet) 