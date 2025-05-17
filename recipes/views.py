from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', context={
        'name':'Silvio Ernesto'
    })

def my_view(request):
    return HttpResponse('Uma linda String')

def nada(request):
    return HttpResponse('Aqui é o inicio')