import json
from django.test import TestCase
from django.urls import reverse
from .models import Recipe
from .forms import RecipeChartForm
from django.contrib.auth import get_user_model
# Import validators
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your tests here.


class RecipeModelTest(TestCase):
    def setUpTestData():
        ingredients_data = [
            {"name": "flour", "quantity": 200, "unit": "g"}, 
            {"name": "milk", "quantity": 300, "unit": "ml"}, 
            {"name": "egg", "quantity": 2, "unit": "pcs"}, 
            {"name": "baking powder", "quantity": 1, "unit": "tsp"}, 
            {"name": "sugar", "quantity": 2, "unit": "tbsp"}
            ]

        # Encode ingredients as JSON
        ingredients_json = json.dumps(ingredients_data)

        # Set up test data object
        Recipe.objects.create(
            name='Classic Pancakes',
            description='Fluffy and light pancakes, perfect for breakfast.',
            prep_time_minutes=10,
            cooking_time_minutes=15,
            difficulty='easy',
            ingredients=ingredients_json
        )

    def test_name(self):
        # Get recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get metadata for 'name' field and use to query its data
        field_label = recipe._meta.get_field('name').verbose_name

        # Compare the name to expected result
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        recipe = Recipe.objects.get(id=1)

        # Get field metadata
        max_length = recipe._meta.get_field('name').max_length

        # Assert that the max length is 120
        self.assertEqual(max_length, 120)

        # Compare the recipes name to <= 120
        self.assertTrue(len(recipe.name) <= 120)

    def test_description_max_length(self):
        recipe = Recipe.objects.get(id=1)

        # Get field metadata
        max_length = recipe._meta.get_field('description').max_length

        # Assert that the max length is 120
        self.assertEqual(max_length, 500)

        # Compare the recipes description to <= 120
        self.assertTrue(len(recipe.description) <= 120)

    def test_cooking_time_validators(self):
        recipe = Recipe.objects.get(id=1)

        # Get field metadata
        cooking_time_minutes = recipe._meta.get_field('cooking_time_minutes')

        # Extract validators from cooking field
        validators = cooking_time_minutes.validators
        # Check if MaxValueValidator is present and its value is 300
        max_value = next(
            (v.limit_value for v in validators if isinstance(v, MaxValueValidator)), None)
        self.assertIsNotNone(
            max_value, "MaxValueValidator is missing from the cooking_time field.")
        self.assertEqual(max_value, 300)

        # Check if MinValueValidator is present and its value is 1
        min_value = next(
            (v.limit_value for v in validators if isinstance(v, MinValueValidator)), None)
        self.assertIsNotNone(
            min_value, "MinValueValidator is missing from the cooking_time field.")
        self.assertEqual(min_value, 1)

    def test_difficulty_max_length(self):
        recipe = Recipe.objects.get(id=1)

        # Get field metadata
        max_length = recipe._meta.get_field('difficulty').max_length

        # Assert that the max length is 12
        self.assertEqual(max_length, 12)

        # Compare the recipes difficulty to <= 12
        self.assertTrue(len(recipe.difficulty) <= 12)

    def test_difficulty_choices_length(self):
        recipe = Recipe.objects.get(id=1)

        # Get difficulty choices
        choices = recipe._meta.get_field('difficulty').choices

        # Check that the amount of choices is 4
        self.assertEqual(len(choices), 4)

    def test_ingredients_format(self):
        recipe = Recipe.objects.get(id=1)

        # Load ingredients, in JSON string
        ingredients_json = recipe.ingredients

        # Convert JSON into python data structure
        # in this case, a list of dictionaries
        try:
            ingredients = json.loads(ingredients_json)
        except json.JSONDecodeError:
            self.fail("Ingredients field does not contain valid JSON.")

        # Check that ingredients is a list
        self.assertIsInstance(
            ingredients, list, "Ingredients should be a list.")

        # Check each ingredient is a valid dictionary with required keys
        required_keys = {"name", "quantity", "unit"}
        for ingredient in ingredients:
            # Check each item in the list is a dictionary
            # One item example:
            # {"name": "flour", "quantity": 200, "unit": "g"}
            self.assertIsInstance(
                ingredient, dict, "Each ingredient should be a dictionary.")
            # Check each dictionary has the required keys
            self.assertTrue(required_keys.issubset(
                ingredient.keys()), f"Each ingredient must include the keys: {required_keys}")
            
    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        # Check that get_absolute_url() takes user to detail page of recipe #1
        # and load URL /recipes/1
        self.assertEqual(recipe.get_absolute_url(), '/recipes/1')

class RecipeChartFormTest(TestCase):        
    def test_chart_form_type(self):
        form = RecipeChartForm()
        self.assertIsInstance(form, RecipeChartForm, 'RecipeChartForm is not of the expected type.')

    def test_chart_type_choices(self):
        form = RecipeChartForm()
        expected_choices = [
            ('#1', 'Bar chart: Ingredient Frequency'),
            ('#2', 'Pie chart: Recipes by Difficulty'),
            ('#3', 'Line chart: Recipes Total Time')
        ]

        # Get choices from form field
        actual_choices = form.fields['chart_type'].choices

        self.assertEqual(actual_choices, expected_choices, 'Chart type choices do not match the expected values.')

class RecipeListViewTest(TestCase):
    def setUp(self):
        # Create user for authentication tests using django's built in user model
        self.user = get_user_model().objects.create(username='testuser')
        self.user.set_password('testpassword')
        self.user.save()
        self.url = reverse('recipes:list')
        
    def setUpTestData():
        ingredients_data = [
            {"name": "flour", "quantity": 200, "unit": "g"}, 
            {"name": "milk", "quantity": 300, "unit": "ml"}, 
            {"name": "egg", "quantity": 2, "unit": "pcs"}, 
            {"name": "baking powder", "quantity": 1, "unit": "tsp"}, 
            {"name": "sugar", "quantity": 2, "unit": "tbsp"}
            ]

        # Encode ingredients as JSON
        ingredients_json = json.dumps(ingredients_data)

        # Set up one recipe data test object
        Recipe.objects.create(
            name='Classic Pancakes',
            description='Fluffy and light pancakes, perfect for breakfast.',
            prep_time_minutes=10,
            cooking_time_minutes=15,
            difficulty='easy',
            ingredients=ingredients_json
        )

    def test_redirect_if_not_authenticated(self):
        # Test that unauthenticated users are redirected to login
        response = self.client.get(self.url)
        self.assertRedirects(response, f'/login/?next={self.url}')

    def test_access_if_authenticated(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')

        # Test that the authenticated user can access the page
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_list.html')

    def test_correct_number_of_recipes_displayed(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        # Check that number of recipes returned matches database entries
        # In this case, 1 from setUpTestData()
        self.assertEqual(len(response.context['recipes']), 1)

class RecipeDetailViewTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

        # Log in the user
        self.client.login(username="testuser", password="testpassword")
        
        ingredients_data = [
            {"name": "flour", "quantity": 200, "unit": "g"}, 
            {"name": "milk", "quantity": 300, "unit": "ml"}, 
            {"name": "egg", "quantity": 2, "unit": "pcs"}, 
            {"name": "baking powder", "quantity": 1, "unit": "tsp"}, 
            {"name": "sugar", "quantity": 2, "unit": "tbsp"}
            ]

        # Encode ingredients as JSON
        ingredients_json = json.dumps(ingredients_data)

        # Set up one recipe data test object
        self.recipe = Recipe.objects.create(
            name='Classic Pancakes',
            description='Fluffy and light pancakes, perfect for breakfast.',
            prep_time_minutes=10,
            cooking_time_minutes=15,
            difficulty='easy',
            ingredients=ingredients_json
        )
        
    def test_recipe_detail_view_successful_response(self):
        # Reverse the URL for detail view
        url = reverse('recipes:detail', kwargs={'pk': self.recipe.id})

        # Make request to reversed URL
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_view_correct_template_used(self):
        url = reverse('recipes:detail', kwargs={'pk': self.recipe.id})

        response = self.client.get(url)

        self.assertTemplateUsed(response, 'recipes/recipe_detail.html')

    def test_recipe_detail_view_context_data(self):
        url = reverse('recipes:detail', kwargs={'pk': self.recipe.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context['recipe'], self.recipe)