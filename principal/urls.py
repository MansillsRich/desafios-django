from django.urls import path
from . import views

urlpatterns = [
    path('', views.saludo),  # Ruta fija
    path('saludo/<str:nombre>/', views.saludar_usuario),  # Ruta con texto
    path('edad/<int:edad>/', views.mostrar_edad),  # Ruta con número
]
