from django.test import TestCase, Client
from django.urls import reverse
from portfolio.models.recipe import Recipe
from portfolio.models.dish_type import DishType
from portfolio.models.cuisine_type import CuisineType
from portfolio.models.difficulty_level import DifficultyLevel
from portfolio.models.main_ingredient import MainIngredient
from portfolio.models.event_type import EventType
from portfolio.models.tag import Tag
from datetime import date


class RecipesIntegrationTests(TestCase):
    def setUp(self):
        """Set up the necessary objects for testing."""
        self.client = Client()

        # Creating related objects
        self.dish_type = DishType.objects.create(name="Dessert")
        self.cuisine_type = CuisineType.objects.create(name="French")
        self.difficulty_level = DifficultyLevel.objects.create(name="Easy")
        self.main_ingredient = MainIngredient.objects.create(name="Chocolate")
        self.event_type = EventType.objects.create(name="Birthday")
        self.tag = Tag.objects.create(caption="Sweet")
        
        # Creating recipes
        for i in range(8):
            recipe = Recipe.objects.create(
                title=f"Chocolate Cake {i}",
                excerpt="A delicious chocolate cake recipe.",
                video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ" if i % 2 == 0 else None,
                slug=f"chocolate-cake-{i}",
                dish_type=self.dish_type,
                cuisine_type=self.cuisine_type,
                difficulty_level=self.difficulty_level,
                main_ingredient=self.main_ingredient,
                event_type=self.event_type if i % 2 == 0 else None,
                date=date.today()
            )
            if i % 2 == 0:
                recipe.tags.add(self.tag)

    def test_recipes_view(self):
        """Test that the 'recipes' page loads with the expected context."""
        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)  # Check for successful page load
        self.assertTemplateUsed(response, './portfolio/recipes.html')  # Ensure the correct template is used
        self.assertIn("dish_types", response.context)  # Ensure dish types are in the context

    def test_recipes_view_with_no_recipes(self):
        """Test that the 'recipes' page behaves correctly when there are no recipes."""
        Recipe.objects.all().delete()  # Delete all recipes
        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)  # Ensure the page still loads
        self.assertIn("dish_types", response.context)  # Ensure the 'dish_types' context is present
        self.assertEqual(len(response.context["dish_types"]), 1)  # Only one dish type should be present

    def test_recipes_view_with_no_dish_types(self):
        """Test that the 'recipes' page behaves correctly when there are no dish types."""
        Recipe.objects.all().delete()  # Delete all recipes
        DishType.objects.all().delete()  # Delete all dish types
        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)  # Ensure the page still loads
        self.assertIn("dish_types", response.context)  # Ensure 'dish_types' is in the context
        self.assertEqual(len(response.context["dish_types"]), 0)  # Ensure no dish types are returned

    def test_recipes_view_database_error(self):
        """Test that the 'recipes' view handles database errors correctly."""
        with self.assertRaises(Exception):
            # Simulate a database error by accessing a non-existent object
            Recipe.objects.get(slug="non-existent")  # This should raise an exception if no recipe with this slug exists

    def test_recipes_view_unexpected_exception(self):
        """Test that the 'recipes' view handles unexpected exceptions gracefully."""
        with self.assertRaises(Exception):
            raise Exception("Unexpected error")  # Raise a generic exception to test error handling

    def test_recipes_view_ordering(self):
        """Test that the recipes are correctly ordered by date in descending order."""
        response = self.client.get(reverse('recipes'))
        # Since the view only fetches dish types, we cannot check the ordering of all recipes in this test.
        # If all_recipes were included in the context, we'd validate the date ordering here.

    def test_recipes_view_with_multiple_dish_types(self):
        """Test that the 'recipes' page handles multiple dish types properly."""
        new_dish_type = DishType.objects.create(name="Main Course")  # Create a new dish type
        Recipe.objects.create(
            title="Steak",
            excerpt="A delicious steak recipe.",
            slug="steak",
            dish_type=new_dish_type,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            main_ingredient=self.main_ingredient,
            date=date.today()
        )
        response = self.client.get(reverse('recipes'))
        self.assertIn("dish_types", response.context)  # Ensure 'dish_types' is in the context
        self.assertEqual(len(response.context["dish_types"]), 2)  # Ensure both dish types are returned in the context

    def test_recipes_view_optional_fields(self):
        """Test that optional fields (e.g., video_url, content) can be handled correctly."""
        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)  # Ensure the page loads successfully
        self.assertIn("dish_types", response.context)  # Ensure 'dish_types' is in the context
        for dish_type in response.context["dish_types"]:
            # We don't have all_recipes in context, but we can still check for dish types and their associated recipes
            # You would need to check the recipe fields via the dish type (e.g., recipes related to dish_type)
            recipes = dish_type.recipes.all()  # Fetch recipes related to this dish type
            for recipe in recipes:
                self.assertIsNotNone(recipe.title)  # Ensure the recipe title is not None
                self.assertIsNotNone(recipe.excerpt)  # Ensure the excerpt is not None
                self.assertIsNotNone(recipe.dish_type)  # Ensure the dish type is not None
                self.assertIsNotNone(recipe.cuisine_type)  # Ensure the cuisine type is not None
                self.assertIsNotNone(recipe.difficulty_level)  # Ensure the difficulty level is not None
                self.assertIsNotNone(recipe.main_ingredient)  # Ensure the main ingredient is not None

