from django.urls import path
from .views import home, RecipeListView

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('list/', RecipeListView.as_view(), name='list')
]