from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html', context={
    'name': 'Silvio Ernesto'
})

def recipes(request):
    return render(request, 'pages/home.html', context={
    'name': 'Silvio Ernesto'
})
