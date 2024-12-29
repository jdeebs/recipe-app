from django.urls import path
from .views import home, RecipeListView

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('recipes/', RecipeListView.as_view(), name='recipes')
]