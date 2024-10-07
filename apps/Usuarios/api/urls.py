from django.urls import path
from apps.Usuarios.api.views import UsuarioViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # type: ignore

router_usuarios = DefaultRouter()
urlpatterns = [
    # Rutas de autenticación
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Rutas para Usuarios
    path('usuarios/', UsuarioViewSet.as_view({'get': 'list'}), name='usuarios-list'),  # Listar usuarios
    path('usuarios/<int:pk>/', UsuarioViewSet.as_view({'get': 'retrieve'}), name='usuarios-detail'),  # Obtener detalle de usuario
    path('usuarios/crear/', UsuarioViewSet.as_view({'post': 'create'}), name='usuarios-create'),  # Crear usuario
    path('usuarios/<int:pk>/actualizar/', UsuarioViewSet.as_view({'put': 'update'}), name='usuarios-update'),  # Actualizar usuario
    path('usuarios/<int:pk>/eliminar/', UsuarioViewSet.as_view({'delete': 'destroy'}), name='usuarios-delete'),  # Eliminar usuario

]
