# JSON for ingredients attributes
import json
from django.db import models
# Import validators
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

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
    name = models.CharField(max_length=120)

    description = models.TextField(max_length=500)

    prep_time_minutes = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(300)
    ],
        help_text="Enter prep time in minutes"
    )

    cooking_time_minutes = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(300)
    ],
        help_text="Enter cooking time in minutes"
    )

    difficulty = models.CharField(
        max_length=12, choices=difficulty_choices, default='easy')

    ingredients = models.TextField(
        help_text="Enter ingredients as a JSON string, e.g., '[{\"name\": \"flour\", \"quantity\": 200, \"unit\": \"g\"}]'"
    )

    def __str__(self):
        return str(self.name)
