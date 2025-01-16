import django_filters
from django.db.models import Q
from .models import Recipe

class RecipeFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_all_fields')

    class Meta:
        model = Recipe
        fields = []

    def filter_all_fields(self, queryset, value):
        # Filters across recipe title, ingredients, and difficulty
        return queryset.filter(
            Q(name__icontains=value) |
            Q(ingredients__icontains=value) |
            Q(difficulty__icontains=value)
        )