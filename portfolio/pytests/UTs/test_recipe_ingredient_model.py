from django.test import TestCase
from portfolio.models.recipe import Recipe
from portfolio.models.recipe_ingredient import RecipeIngredient
from django.test import TestCase
from portfolio.models.recipe import Recipe
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from portfolio.models.recipe import Recipe
from portfolio.models.cuisine_type import CuisineType
from portfolio.models.difficulty_level import DifficultyLevel
from portfolio.models.dish_type import DishType
from portfolio.models.main_ingredient import MainIngredient
from portfolio.models.event_type import EventType


class RecipeIngredientModelTest(TestCase):
    def setUp(self):
        # Create a sample recipe
        # Set up required related objects for the Recipe model
        self.dish_type = DishType.objects.create(name="Main Course")
        self.main_ingredient = MainIngredient.objects.create(name="Chicken")
        self.cuisine_type = CuisineType.objects.create(name="Italian")
        self.difficulty_level = DifficultyLevel.objects.create(name="Easy")
        self.event_type = EventType.objects.create(name="Dinner Party")
        # Set up a Recipe instance that we will use to associate with RecipeImage
        self.recipe = Recipe.objects.create(
            title="Spaghetti Carbonara",
            excerpt="A classic Italian pasta dish with eggs, cheese, pancetta, and pepper.",
            image="carbonara.jpg",
            slug=slugify("Spaghetti Carbonara"),
            content="Cook pasta, fry pancetta, mix with eggs and cheese, combine and serve.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            event_type=self.event_type,
        )

    # Test if a RecipeIngredient object can be created successfully
    def test_create_recipe_ingredient(self):
        ingredient = RecipeIngredient.objects.create(name="Sugar", recipe=self.recipe)
        self.assertEqual(ingredient.name, "Sugar")
        self.assertEqual(ingredient.recipe, self.recipe)

    # Test the string representation of a RecipeIngredient object
    def test_string_representation(self):
        ingredient = RecipeIngredient.objects.create(name="Flour", recipe=self.recipe)
        self.assertEqual(str(ingredient), "Flour")

    # Test if deleting a recipe also deletes its associated ingredients due to CASCADE constraint
    def test_recipe_foreign_key_constraint(self):
        ingredient = RecipeIngredient.objects.create(name="Salt", recipe=self.recipe)
        self.recipe.delete()
        
        # The ingredient should be deleted due to CASCADE constraint
        self.assertFalse(RecipeIngredient.objects.filter(id=ingredient.id).exists())

    # Test that the name field respects the max_length constraint (80 characters)
    def test_max_length_name(self):
        ingredient = RecipeIngredient.objects.create(name="A" * 80, recipe=self.recipe)
        self.assertEqual(len(ingredient.name), 80)

    # Test that an empty name is not allowed and raises a ValidationError
    def test_blank_name_not_allowed(self):
        ingredient = RecipeIngredient(name="", recipe=self.recipe)
        with self.assertRaises(ValidationError):
            ingredient.full_clean()  # Ensures Django validation is triggered
