from django.shortcuts import render
from utils.recipes.factory import make_recipe

def home(request):
    return render(request, 'pages/home.html', context={
    'recipes': [make_recipe() for i in range(10)],
})
def recipes(request, id):
    return render(request, 'pages/recipe-view.html', context={
    'recipe': make_recipe(),
    'is_detail_page': True
})

#def recipes_by_category(request, category):
#   return HttpResponse(f"Teste : {category}")