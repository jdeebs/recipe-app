# Run the following commands to add recipes to the database:
# ** Make sure you're in the project src folder **
# python manage.py shell
# exec(open('seed_recipes.py').read())

from recipes.models import Recipe
import json

recipes = [
    # Example recipe input format:
    # "pic" attribute is omitted to be uploaded manually,
    # defaults to the no_picture.svg file
    {
        "name": "Classic Pancakes",
        "description": "Fluffy and light pancakes, perfect for breakfast.",
        "prep_time_minutes": 10,
        "cooking_time_minutes": 15,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "flour", "quantity": 200, "unit": "g"},
            {"name": "milk", "quantity": 300, "unit": "ml"},
            {"name": "egg", "quantity": 2, "unit": "pcs"},
            {"name": "baking powder", "quantity": 1, "unit": "tsp"},
            {"name": "sugar", "quantity": 2, "unit": "tbsp"}
        ]),
    },
    {
        "name": "Spaghetti Bolognese",
        "description": "A classic Italian pasta dish with rich meat sauce.",
        "prep_time_minutes": 15,
        "cooking_time_minutes": 45,
        "difficulty": "medium",
        "ingredients": json.dumps([
            {"name": "spaghetti", "quantity": 200, "unit": "g"},
            {"name": "ground beef", "quantity": 300, "unit": "g"},
            {"name": "onion", "quantity": 1, "unit": "pcs"},
            {"name": "garlic", "quantity": 2, "unit": "cloves"},
            {"name": "tomato sauce", "quantity": 400, "unit": "ml"}
        ]),
    },
    {
        "name": "Vegetable Stir Fry",
        "description": "Quick and easy stir fry with fresh vegetables.",
        "prep_time_minutes": 10,
        "cooking_time_minutes": 10,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "broccoli", "quantity": 150, "unit": "g"},
            {"name": "carrot", "quantity": 2, "unit": "pcs"},
            {"name": "bell pepper", "quantity": 1, "unit": "pcs"},
            {"name": "soy sauce", "quantity": 2, "unit": "tbsp"},
            {"name": "garlic", "quantity": 1, "unit": "clove"}
        ]),
    },
    {
        "name": "Chicken Curry",
        "description": "A flavorful curry with tender chicken pieces.",
        "prep_time_minutes": 20,
        "cooking_time_minutes": 40,
        "difficulty": "intermediate",
        "ingredients": json.dumps([
            {"name": "chicken breast", "quantity": 400, "unit": "g"},
            {"name": "coconut milk", "quantity": 200, "unit": "ml"},
            {"name": "onion", "quantity": 1, "unit": "pcs"},
            {"name": "curry powder", "quantity": 2, "unit": "tbsp"},
            {"name": "ginger", "quantity": 1, "unit": "tsp"}
        ]),
    },
    {
        "name": "Chocolate Chip Cookies",
        "description": "Chewy cookies loaded with chocolate chips.",
        "prep_time_minutes": 15,
        "cooking_time_minutes": 12,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "butter", "quantity": 100, "unit": "g"},
            {"name": "sugar", "quantity": 150, "unit": "g"},
            {"name": "flour", "quantity": 200, "unit": "g"},
            {"name": "chocolate chips", "quantity": 150, "unit": "g"},
            {"name": "egg", "quantity": 1, "unit": "pcs"}
        ]),
    }
]

for recipe_data in recipes:
    Recipe.objects.create(**recipe_data)
