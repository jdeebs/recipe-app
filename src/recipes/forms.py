from django import forms

CHART__CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

class RecipeChartForm(forms.Form):
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)