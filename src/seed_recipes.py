# Run the following commands to add recipes to the database:
# ** Make sure you're in the project src folder **
# python manage.py shell
# exec(open('seed_recipes.py').read())

from recipes.models import Recipe
import json

recipes = [
    # Example recipe input format:
    # "pic" attribute can be omitted to be uploaded manually,
    # defaults to the no_picture.svg file
    {
        "name": "Beef Tacos",
        "description": "Mexican-style tacos filled with seasoned beef and fresh toppings.",
        "prep_time_minutes": 15,
        "cooking_time_minutes": 10,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "ground beef", "quantity": 300, "unit": "g"},
            {"name": "taco seasoning", "quantity": 1, "unit": "tbsp"},
            {"name": "tortillas", "quantity": 6, "unit": "pcs"},
            {"name": "lettuce", "quantity": 1, "unit": "cup"},
            {"name": "cheese", "quantity": 100, "unit": "g"}
        ]),
        "pic": "recipes/beef-tacos.jpg",
    },
    {
        "name": "Greek Salad",
        "description": "A fresh and vibrant salad with classic Mediterranean flavors.",
        "prep_time_minutes": 10,
        "cooking_time_minutes": 0,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "cucumber", "quantity": 1, "unit": "pcs"},
            {"name": "tomatoes", "quantity": 2, "unit": "pcs"},
            {"name": "feta cheese", "quantity": 100, "unit": "g"},
            {"name": "olives", "quantity": 50, "unit": "g"},
            {"name": "olive oil", "quantity": 2, "unit": "tbsp"}
        ]),
        "pic": "recipes/greek-salad.jpg",
    },
    {
        "name": "Minestrone Soup",
        "description": "A hearty Italian vegetable soup with beans and pasta.",
        "prep_time_minutes": 15,
        "cooking_time_minutes": 30,
        "difficulty": "medium",
        "ingredients": json.dumps([
            {"name": "carrot", "quantity": 2, "unit": "pcs"},
            {"name": "celery", "quantity": 2, "unit": "stalks"},
            {"name": "onion", "quantity": 1, "unit": "pcs"},
            {"name": "pasta", "quantity": 100, "unit": "g"},
            {"name": "beans", "quantity": 200, "unit": "g"}
        ]),
        "pic": "recipes/minestrone-soup.jpg",
    },
    {
        "name": "Shrimp Scampi",
        "description": "Juicy shrimp in a garlic and butter sauce over pasta.",
        "prep_time_minutes": 10,
        "cooking_time_minutes": 15,
        "difficulty": "medium",
        "ingredients": json.dumps([
            {"name": "shrimp", "quantity": 300, "unit": "g"},
            {"name": "garlic", "quantity": 3, "unit": "cloves"},
            {"name": "butter", "quantity": 100, "unit": "g"},
            {"name": "white wine", "quantity": 100, "unit": "ml"},
            {"name": "pasta", "quantity": 200, "unit": "g"}
        ]),
        "pic": "recipes/shrimp-scampi.jpg",
    },
    {
        "name": "Vegetable Lasagna",
        "description": "Layered lasagna with a variety of fresh vegetables.",
        "prep_time_minutes": 20,
        "cooking_time_minutes": 50,
        "difficulty": "hard",
        "ingredients": json.dumps([
            {"name": "lasagna noodles", "quantity": 250, "unit": "g"},
            {"name": "ricotta cheese", "quantity": 200, "unit": "g"},
            {"name": "spinach", "quantity": 150, "unit": "g"},
            {"name": "zucchini", "quantity": 1, "unit": "pcs"},
            {"name": "tomato sauce", "quantity": 400, "unit": "ml"}
        ]),
        "pic": "recipes/vegetable-lasagna.jpg",
    },
    {
        "name": "Banana Smoothie",
        "description": "A creamy and healthy banana smoothie.",
        "prep_time_minutes": 5,
        "cooking_time_minutes": 0,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "banana", "quantity": 2, "unit": "pcs"},
            {"name": "milk", "quantity": 300, "unit": "ml"},
            {"name": "yogurt", "quantity": 100, "unit": "g"},
            {"name": "honey", "quantity": 1, "unit": "tbsp"},
            {"name": "ice cubes", "quantity": 5, "unit": "pcs"}
        ]),
        "pic": "recipes/banana-smoothie.jpg",
    },
    {
        "name": "Caesar Salad",
        "description": "Crispy romaine lettuce tossed with Caesar dressing and croutons.",
        "prep_time_minutes": 10,
        "cooking_time_minutes": 0,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "romaine lettuce", "quantity": 200, "unit": "g"},
            {"name": "Caesar dressing", "quantity": 50, "unit": "ml"},
            {"name": "croutons", "quantity": 100, "unit": "g"},
            {"name": "Parmesan cheese", "quantity": 50, "unit": "g"},
            {"name": "lemon juice", "quantity": 1, "unit": "tbsp"}
        ]),
        "pic": "recipes/caesar-salad.jpg",
    },
    {
        "name": "Margherita Pizza",
        "description": "Classic pizza with fresh tomato, mozzarella, and basil.",
        "prep_time_minutes": 20,
        "cooking_time_minutes": 15,
        "difficulty": "medium",
        "ingredients": json.dumps([
            {"name": "pizza dough", "quantity": 1, "unit": "pcs"},
            {"name": "tomato sauce", "quantity": 150, "unit": "ml"},
            {"name": "mozzarella cheese", "quantity": 200, "unit": "g"},
            {"name": "fresh basil leaves", "quantity": 10, "unit": "pcs"},
            {"name": "olive oil", "quantity": 1, "unit": "tbsp"}
        ]),
        "pic": "recipes/margherita-pizza.jpg",
    },
    {
        "name": "Lemon Garlic Shrimp",
        "description": "Succulent shrimp sautéed in a lemon garlic butter sauce.",
        "prep_time_minutes": 10,
        "cooking_time_minutes": 10,
        "difficulty": "easy",
        "ingredients": json.dumps([
            {"name": "shrimp", "quantity": 300, "unit": "g"},
            {"name": "garlic", "quantity": 3, "unit": "cloves"},
            {"name": "butter", "quantity": 2, "unit": "tbsp"},
            {"name": "lemon juice", "quantity": 2, "unit": "tbsp"},
            {"name": "parsley", "quantity": 1, "unit": "tbsp"}
        ]),
        "pic": "recipes/lemon-garlic-shrimp.jpg",
    },
    {
        "name": "Vegetarian Chili",
        "description": "Hearty chili packed with beans, veggies, and spices.",
        "prep_time_minutes": 15,
        "cooking_time_minutes": 30,
        "difficulty": "medium",
        "ingredients": json.dumps([
            {"name": "kidney beans", "quantity": 400, "unit": "g"},
            {"name": "black beans", "quantity": 400, "unit": "g"},
            {"name": "onion", "quantity": 1, "unit": "pcs"},
            {"name": "bell pepper", "quantity": 2, "unit": "pcs"},
            {"name": "chili powder", "quantity": 1, "unit": "tbsp"}
        ]),
        "pic": "recipes/vegetarian-chili.jpg",
    },
]

for recipe_data in recipes:
    Recipe.objects.create(**recipe_data)
