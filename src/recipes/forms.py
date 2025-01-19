from django import forms

CHART__CHOICES = (
    ('#1', 'Bar chart: Ingredient Frequency'),
    ('#2', 'Pie chart: Recipes by Difficulty'),
    ('#3', 'Line chart: Recipes Total Time')
)

class RecipeChartForm(forms.Form):
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)