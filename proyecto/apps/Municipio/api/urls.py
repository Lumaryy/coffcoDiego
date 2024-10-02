from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Municipio.api.views import MunicipioViewSet

router_municipio= DefaultRouter()
router_municipio.register(prefix='municipio', basename='municipio', viewset=MunicipioViewSet)
