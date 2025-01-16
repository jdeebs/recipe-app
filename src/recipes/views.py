from django.shortcuts import render
from django.views.generic import ListView, DetailView
# For search functionality
from django_filters.views import FilterView
from .filters import RecipeFilter
# To protect a CBV
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView, FilterView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'
    filterset_class = RecipeFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_placeholder'] = 'Search recipes by title, ingredients, or difficulty'
        return context

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'