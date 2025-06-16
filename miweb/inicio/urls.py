from django.urls import path
from . import views

urlpatterns = [
    path('', views.curriculum_view, name='home'),
    path('curriculum/', views.curriculum_view, name='curriculum'),
]
