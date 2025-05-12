from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from recipes.views import home, nada, my_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', my_view),
    path('', home),
    path('home/', nada)
]

