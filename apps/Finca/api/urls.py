from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Finca.api.views import FincaViewSet

router_finca = DefaultRouter()
router_finca.register(prefix='finca', basename='finca', viewset=FincaViewSet)
