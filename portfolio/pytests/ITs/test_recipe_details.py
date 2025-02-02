from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db import IntegrityError
from portfolio.models.recipe import Recipe
from portfolio.models.dish_type import DishType
from portfolio.models.main_ingredient import MainIngredient
from portfolio.models.cuisine_type import CuisineType
from portfolio.models.recipe_ingredient import RecipeIngredient
from portfolio.models.difficulty_level import DifficultyLevel
from portfolio.models.event_type import EventType
from portfolio.models.tag import Tag
from django.conf import settings

class RecipeDetailViewTest(TestCase):

    def setUp(self):
        # Create related model instances for foreign keys
        self.dish_type = DishType.objects.create(name="Main Course")
        self.main_ingredient = MainIngredient.objects.create(name="Chicken")
        self.cuisine_type = CuisineType.objects.create(name="Italian")
        self.difficulty_level = DifficultyLevel.objects.create(name="Easy")
        self.event_type = EventType.objects.create(name="Dinner")
        self.tag = Tag.objects.create(caption="Quick")
        
        # Create a test recipe
        self.recipe = Recipe.objects.create(
            title="Chicken Parmesan",
            excerpt="A quick and easy chicken parmesan recipe.",
            slug="chicken-parmesan",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            event_type=self.event_type
        )
        self.recipe.tags.add(self.tag)

    def test_recipe_detail_page_renders(self):
        # Test if recipe detail page renders correctly
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.title)
        self.assertContains(response, self.recipe.content)

    def test_missing_recipe_returns_404(self):
        # Test if a missing recipe returns a 404 error
        response = self.client.get(reverse('recipe_detail', args=["non-existing-slug"]))
        self.assertEqual(response.status_code, 404)

    def test_recipe_video_url_is_embedded(self):
        # Test if the recipe's video URL is properly embedded in the page
        self.recipe.video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        self.recipe.save()
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.slug]))
        self.assertContains(response, '<iframe width="100%" height="415"')
        self.assertContains(response, self.recipe.video_url)

    def test_recipe_image_is_displayed(self):
        # Test if the recipe image is displayed when there is no video URL
        self.recipe.image = "recipe-image.jpg"
        self.recipe.save()
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.slug]))
        self.assertContains(response, "recipe-image.jpg")

    def test_similar_recipes_displayed(self):
        # Test if similar recipes are displayed correctly
        similar_recipe = Recipe.objects.create(
            title="Chicken Alfredo",
            slug="chicken-alfredo",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.slug]))
        self.assertContains(response, similar_recipe.title)

    def test_recipe_tags_are_rendered(self):
        # Test if tags are rendered correctly
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.slug]))
        self.assertContains(response, self.tag.caption)

    def test_ingredients_are_displayed(self):
        # Test if ingredients are displayed in the sidebar
        # Assume there is a model Ingredient (not provided in your code snippet)
        # Create ingredients for the recipe
        ingredient = RecipeIngredient.objects.create(recipe=self.recipe, name="Bread Crumbs")
        self.recipe.ingredients.add(ingredient)
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.slug]))
        self.assertContains(response, ingredient.name)

    def test_recipe_with_missing_cover_picture(self):
        # Test if recipe without cover picture still renders without error
        self.recipe.cover_picture = None
        self.recipe.save()
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.slug]))
        self.assertEqual(response.status_code, 200)  # It should still render the page

    def test_invalid_video_url_does_not_break_page(self):
        # Test that an invalid video URL doesn't break the page
        self.recipe.video_url = "invalid-url"
        self.recipe.save()
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.slug]))
        self.assertContains(response, self.recipe.title)

    def test_recipe_content_renders_correctly(self):
        # Test if recipe content renders properly
        self.recipe.content = "<p>Step 1: Prepare chicken.</p>"
        self.recipe.save()
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.slug]))
        self.assertContains(response, "Step 1: Prepare chicken.")
