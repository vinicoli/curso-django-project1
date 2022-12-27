from django.http import HttpResponse
from django.shortcuts import render


def home(request):  # HOME
    return render(request, 'recipes/pages/home.html')

def recipe(request, id):  # HOME
    return render(request, 'recipes/pages/recipe-view.html')
