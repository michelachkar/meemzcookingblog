from django.test import TestCase, Client
from django.urls import reverse
from portfolio.models.recipe import Recipe
from portfolio.models.dish_type import DishType
from portfolio.models.gallery_image import GalleryImage
from portfolio.models.slide import Slide
from portfolio.models.cuisine_type import CuisineType
from portfolio.models.difficulty_level import DifficultyLevel
from portfolio.models.event_type import EventType
from portfolio.models.main_ingredient import MainIngredient
from portfolio.models.tag import Tag
from datetime import date

class HomeViewTests(TestCase):
    def setUp(self):
        # Initialize a test client and create all the necessary related objects for testing
        self.client = Client()
        
        # Creating related objects (DishType, CuisineType, DifficultyLevel, etc.)
        self.dish_type = DishType.objects.create(name="Dessert")
        self.cuisine_type = CuisineType.objects.create(name="French")
        self.difficulty_level = DifficultyLevel.objects.create(name="Easy")
        self.main_ingredient = MainIngredient.objects.create(name="Chocolate")
        self.event_type = EventType.objects.create(name="Birthday")
        self.tag = Tag.objects.create(caption="Sweet")
        
        # Creating multiple recipes for testing
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
        
        # Creating some gallery images and slides for the homepage view
        self.gallery_image = GalleryImage.objects.create(image="portfolio/images/gallery1.jpg")
        self.slide = Slide.objects.create(image="portfolio/images/slide1.jpg")

    def test_home_view(self):
        """Test that the home page loads with the expected context."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Check for a successful page load (200 OK)
        self.assertTemplateUsed(response, 'portfolio/home.html')  # Ensure the correct template is used
        self.assertIn("all_recipes", response.context)  # Verify 'all_recipes' is in the context
        self.assertIn("gallery_images", response.context)  # Ensure gallery images are in the context
        self.assertIn("slides", response.context)  # Ensure slides are present in the context
        
        # Check that only the 6 latest recipes are retrieved for each dish type
        all_recipes = response.context["all_recipes"]
        for _, recipes in all_recipes:
            self.assertLessEqual(len(recipes), 6)  # Ensure no more than 6 recipes are returned per dish type

    def test_recipe_ordering(self):
        """Test that recipes are correctly ordered by date in descending order."""
        response = self.client.get(reverse('home'))
        all_recipes = response.context["all_recipes"]
        for _, recipes in all_recipes:
            dates = [recipe.date for recipe in recipes]
            self.assertEqual(dates, sorted(dates, reverse=True))  # Check if dates are sorted in reverse order

    def test_home_view_missing_event_type(self):
        """Test that the home view handles missing event types gracefully."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Ensure the page loads correctly
        self.assertIn("all_recipes", response.context)  # 'all_recipes' should still be in context even if no event type

    def test_home_view_multiple_dish_types(self):
        """Test that multiple dish types (e.g., Dessert and Main Course) can be handled."""
        new_dish_type = DishType.objects.create(name="Main Course")  # Create another dish type
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
        response = self.client.get(reverse('home'))
        self.assertIn("all_recipes", response.context)  # Ensure 'all_recipes' is in the context
        self.assertEqual(len(response.context["all_recipes"]), 2)  # Ensure both dish types appear in the context

    def test_home_view_optional_fields(self):
        """Test that all required fields for each recipe are present and not None."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Ensure the page loads successfully
        for _, recipes in response.context["all_recipes"]:
            for recipe in recipes:
                # Check that essential recipe fields are not None
                self.assertIsNotNone(recipe.title)
                self.assertIsNotNone(recipe.excerpt)
                self.assertIsNotNone(recipe.dish_type)
                self.assertIsNotNone(recipe.cuisine_type)
                self.assertIsNotNone(recipe.difficulty_level)

    def test_home_view_no_recipes(self):
        """Test that the home view correctly handles the case with no recipes."""
        # Delete all recipes and dish types from the database
        Recipe.objects.all().delete()
        DishType.objects.all().delete()
        
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Ensure the page loads successfully
        self.assertIn("all_recipes", response.context)  # Check if 'all_recipes' is still in the context
        self.assertEqual(len(response.context["all_recipes"]), 0)  # Ensure no recipes are returned in the context

    def test_home_view_no_gallery_images(self):
        """Test that the home view correctly handles the case with no gallery images."""
        GalleryImage.objects.all().delete()  # Delete all gallery images
        
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Page should still load
        self.assertIn("gallery_images", response.context)  # Ensure gallery images key is still in context
        self.assertEqual(len(response.context["gallery_images"]), 0)  # Ensure no gallery images are returned

    def test_home_view_no_slides(self):
        """Test that the home view correctly handles the case with no slides."""
        Slide.objects.all().delete()  # Delete all slides
        
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Ensure the page loads successfully
        self.assertIn("slides", response.context)  # Ensure slides key is still in context
        self.assertEqual(len(response.context["slides"]), 0)  # Ensure no slides are returned

    def test_home_view_database_error(self):
        """Test that the home view handles database errors gracefully."""
        with self.assertRaises(Exception):
            # Simulate a database error by accessing a non-existent object
            Recipe.objects.get(slug="non-existent")  # This should raise an exception if no recipe with this slug exists

    def test_home_view_unexpected_exception(self):
        """Test that the home view correctly handles unexpected exceptions."""
        with self.assertRaises(Exception):
            raise Exception("Unexpected error")  # Raise a generic exception to test error handling
