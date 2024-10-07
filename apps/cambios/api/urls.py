from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cambios.api.views import CambiosViewSet

router_cambios = DefaultRouter()
router_cambios.register(prefix='cambios', basename='cambios', viewset=CambiosViewSet)

urlpatterns = [
    path('', include(router_cambios.urls)),
]