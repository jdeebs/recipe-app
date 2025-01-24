# JSON for ingredients attributes
import json
from django.db import models
# Import validators
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
# Import needed for get_absolute_url() using primary key <pk>
from django.shortcuts import reverse

# Create your models here.
difficulty_choices = (
    ('easy',
     'Easy'),
    ('medium',
     'Medium'),
    ('intermediate',
     'Intermediate'),
    ('hard',
     'Hard')
)

# Validate ingredients as JSON


def validate_ingredients(value):
    try:
        # Attempt to parse as JSON
        ingredients = json.loads(value)
        if not isinstance(ingredients, list):
            raise ValidationError(
                "Ingredients must be a list of dictionaries.")
        for ingredient in ingredients:
            if not all(key in ingredient for key in ["name", "quantity", "unit"]):
                raise ValidationError(
                    "Each ingredient must include 'name', 'quantity', and 'unit'.")
    except (ValueError, TypeError):
        raise ValidationError("Ingredients must be valid JSON.")


class Recipe(models.Model):
    name = models.CharField(max_length=120, default="Unnamed Recipe")

    description = models.TextField(
        max_length=500, default="No description available.")

    prep_time_minutes = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(300)
    ],
        help_text="Enter prep time in minutes",
        default=10
    )

    cooking_time_minutes = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(300)
    ],
        help_text="Enter cooking time in minutes",
        default=20
    )

    difficulty = models.CharField(
        max_length=12, choices=difficulty_choices, default='easy')

    ingredients = models.TextField(
        default=json.dumps([{"name": "water", "quantity": 1, "unit": "cup"}]),
        validators=[validate_ingredients],
        help_text="Enter ingredients as a JSON string, e.g., '[{\"name\": \"flour\", \"quantity\": 200, \"unit\": \"g\"}]'"
    )

    pic = models.ImageField(upload_to='recipes', default='no_image.svg')

    class Meta:
        # Order recipes alphabetically by name
        ordering = ['name']

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})
    
    def parsed_ingredients(self):
        try:
            return json.loads(self.ingredients)
        except json.JSONDecodeError:
            return []
        
    def total_time(self):
        return self.prep_time_minutes + self.cooking_time_minutes