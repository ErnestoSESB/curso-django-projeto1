from django.urls import path
from . import views

urlpatterns = [
    path('recipes/<int:id>', views.recipes),
    path('', views.home),
    path('recipes/<int:id>', views