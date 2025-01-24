from django.shortcuts import render
from django.views.generic import DetailView
# For search functionality
from django_filters.views import FilterView
from .filters import RecipeFilter
# To protect a CBV
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
# For chart visualization
import pandas as pd
from .utils import get_chart
from .forms import RecipeChartForm
# For pagination
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, FilterView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'
    filterset_class = RecipeFilter
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Placeholder text for search field
        context['search_placeholder'] = 'Search recipes by title, ingredients, or difficulty'

        form = RecipeChartForm(self.request.GET or None)
        # Add form to context
        context['form'] = form
        chart = None

        # Get filtered queryset
        filtered_recipes = self.filterset.qs
        # Paginate filtered recipes
        paginator = Paginator(filtered_recipes, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Add the paginated recipes (page_obj) to context
        context['recipes'] = page_obj
        context['paginator'] = paginator
        context['page_obj'] = page_obj

        # Get ingredient names
        ingredient_names = []
        for recipe in filtered_recipes:
            for ingredient in recipe.parsed_ingredients():
                ingredient_names.append(ingredient['name'].capitalize())
        ingredient_names.sort()
        
        # Convert queryset to a Pandas DataFrame
        recipe_data = pd.DataFrame([
            {
                'name': recipe.name,
                'ingredients': [ingredient['name'].capitalize() for ingredient in recipe.parsed_ingredients()],
                'difficulty': recipe.difficulty,
                'total_time': recipe.total_time()
            }
            for recipe in filtered_recipes
        ]
        )

        # Check if the form is valid
        if form.is_valid() and not recipe_data.empty:
            # Retrieve the selected chart type
            chart_type = form.cleaned_data.get('chart_type')

            # Generate the chart
            chart = get_chart(chart_type, recipe_data)
            context['chart'] = chart
        else:
            context['chart'] = None
        return context
    
    def get_queryset(self):
        queryset = Recipe.objects.all()  # Or apply any filters here
        print("Queryset length:", len(queryset))
        return queryset


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'