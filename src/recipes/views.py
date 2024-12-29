from django.shortcuts import render
from django.views.generic import ListView
from .models import Recipe

# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'