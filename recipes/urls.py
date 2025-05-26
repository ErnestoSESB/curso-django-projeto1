from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipes, name="recipe"),
    #path('recipes/category/<str:category>/', views.recipes_by_category, name="recipes-category")
]

