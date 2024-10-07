from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Rol.api.views import RolViewSet


router_rol = DefaultRouter()
router_rol.register(r'roles', RolViewSet, basename='roles')


urlpatterns = [
    path('roles/', RolViewSet.as_view({'get': 'list'}), name='roles-list'),  # Listar roles
    path('roles/<int:pk>/', RolViewSet.as_view({'get': 'retrieve'}), name='roles-detail'),  # Obtener detalle de rol
    path('roles/crear/', RolViewSet.as_view({'post': 'create'}), name='roles-create'),  # Crear rol
    path('roles/<int:pk>/actualizar/', RolViewSet.as_view({'put': 'update'}), name='roles-update'),  # Actualizar rol
    path('roles/<int:pk>/eliminar/', RolViewSet.as_view({'delete': 'destroy'}), name='roles-delete'),  # Eliminar rol

]

