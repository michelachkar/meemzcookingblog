from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from portfolio.models.recipe import Recipe
from portfolio.models.cuisine_type import CuisineType
from portfolio.models.difficulty_level import DifficultyLevel
from portfolio.models.dish_type import DishType
from portfolio.models.main_ingredient import MainIngredient
from portfolio.models.event_type import EventType
from portfolio.models.tag import Tag
from django.db.models import ProtectedError
from django.core.files.uploadedfile import SimpleUploadedFile


class RecipeModelTest(TestCase):

    def setUp(self):
        """Set up required related objects for the Recipe model."""
        self.dish_type = DishType.objects.create(name="Main Course")
        self.main_ingredient = MainIngredient.objects.create(name="Chicken")
        self.cuisine_type = CuisineType.objects.create(name="Italian")
        self.difficulty_level = DifficultyLevel.objects.create(name="Easy")
        self.event_type = EventType.objects.create(name="Dinner Party")

    def test_create_recipe(self):
        """Ensure that the title and slug are saved correctly."""
        recipe = Recipe.objects.create(
            title="Spaghetti Carbonara",
            excerpt="A classic Italian pasta dish with eggs, cheese, pancetta, and pepper.",
            image=SimpleUploadedFile("carbonara.jpg", b"image_data"),
            slug=slugify("Spaghetti Carbonara"),
            content="Cook pasta, fry pancetta, mix with eggs and cheese, combine and serve.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            event_type=self.event_type,
        )
        self.assertEqual(recipe.title, "Spaghetti Carbonara")
        self.assertEqual(recipe.slug, "spaghetti-carbonara")

    def test_max_length_constraints(self):
        """Test maximum length constraints for title, excerpt, and slug."""
        recipe = Recipe(
            title="T" * 151,  # Exceeds max length
            excerpt="E" * 201,  # Exceeds max length
            slug="S" * 256,  # Exceeds max length
            content="Valid content over 10 chars.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        with self.assertRaises(ValidationError):
            recipe.full_clean()

    def test_recipe_slug_unique(self):
        """Test that duplicate slugs raise an error."""
        Recipe.objects.create(
            title="Spaghetti Carbonara",
            excerpt="A classic Italian pasta dish.",
            image=SimpleUploadedFile("carbonara.jpg", b"image_data"),
            slug="spaghetti-carbonara",
            content="Step-by-step guide.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        with self.assertRaises(ValidationError):
            duplicate_recipe = Recipe(
                title="Another Carbonara",
                excerpt="A variation of Carbonara.",
                image=SimpleUploadedFile("carbonara2.jpg", b"image_data"),
                slug="spaghetti-carbonara",  # Duplicate slug
                content="Different step-by-step guide.",
                dish_type=self.dish_type,
                main_ingredient=self.main_ingredient,
                cuisine_type=self.cuisine_type,
                difficulty_level=self.difficulty_level,
            )
            duplicate_recipe.full_clean()

    def test_auto_date_field(self):
        """Ensure that the `date` field is automatically set."""
        recipe = Recipe.objects.create(
            title="Auto Date Test",
            excerpt="Checking date field behavior.",
            image=SimpleUploadedFile("date.jpg", b"image_data"),
            slug="auto-date-test",
            content="Some valid content here.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        self.assertIsNotNone(recipe.date)

    def test_slug_special_characters(self):
        """Test that special characters in the title are sanitized in the slug."""
        recipe = Recipe.objects.create(
            title="Special @Character #Recipe!",
            excerpt="Testing special characters in slug.",
            image=SimpleUploadedFile("special_characters.jpg", b"image_data"),
            slug=slugify("Special @Character #Recipe!"),
            content="Some content with special characters.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        self.assertEqual(recipe.slug, "special-character-recipe")

    def test_foreign_key_protection(self):
        """Test that referenced foreign keys are protected from deletion."""
        recipe = Recipe.objects.create(
            title="Special @Character #Recipe!",
            excerpt="Testing special characters in slug.",
            image=SimpleUploadedFile("special_characters.jpg", b"image_data"),
            slug=slugify("Special @Character #Recipe!"),
            content="Some content with special characters.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        with self.assertRaises(ProtectedError):
            self.difficulty_level.delete()
        with self.assertRaises(ProtectedError):
            self.dish_type.delete()
        with self.assertRaises(ProtectedError):
            self.main_ingredient.delete()
        with self.assertRaises(ProtectedError):
            self.cuisine_type.delete()

    def test_foreign_key_set_null_event_type(self):
        """Ensure that deleting an EventType sets the related recipe’s event_type to NULL."""
        event_type = EventType.objects.create(name="Birthday")
        recipe = Recipe.objects.create(
            title="Birthday Cake",
            excerpt="A delicious birthday cake recipe.",
            image=SimpleUploadedFile("cake.jpg", b"image_data"),
            slug="birthday-cake",
            content="Bake the cake.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            event_type=event_type,
        )
        event_type.delete()
        recipe.refresh_from_db()
        self.assertIsNone(recipe.event_type)

    def test_image_upload_path(self):
        """Test that images are stored in the correct directory."""
        file = SimpleUploadedFile("test_image.jpg", b"image_data")
        recipe = Recipe.objects.create(
            title="Recipe With Image",
            excerpt="A recipe with an uploaded image.",
            image=file,
            slug="recipe-with-image",
            content="Recipe content goes here.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        self.assertTrue(recipe.image.name.startswith("recipe/"))

    # Test for valid video URL
    def test_valid_video_url(self):
        valid_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        recipe = Recipe.objects.create(
            title="Special @Character #Recipe!",
            excerpt="Testing special characters in slug.",
            image=SimpleUploadedFile("special_characters.jpg", b"image_data"),
            slug=slugify("Special @Character #Recipe!"),
            content="Some content with special characters.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            video_url=valid_url
        )
        self.assertEqual(recipe.video_url, valid_url)

    # Test for invalid video URL
    def test_invalid_video_url(self):
        invalid_url = "invalid_url"
        recipe = Recipe(
            title="Invalid Video URL",
            excerpt="This should fail",
            image="video_fail.jpg",
            slug="invalid-video-url",
            content="Some content",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            video_url=invalid_url
        )
        with self.assertRaises(ValidationError):
            recipe.full_clean()

    # Test for empty video URL
    def test_empty_video_url(self):
        recipe = Recipe.objects.create(
            title="Recipe Without Video URL",
            excerpt="Recipe without a video URL.",
            image="no_video.jpg",
            slug="recipe-without-video-url",
            content="Some content",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            video_url=None  # No video URL specified
        )
        self.assertIsNone(recipe.video_url)

    # Test for non-YouTube video URL
    def test_non_youtube_video_url(self):
        valid_url = "https://vimeo.com/123456"
        recipe = Recipe.objects.create(
            title="Recipe With Vimeo Video URL",
            excerpt="Recipe with a Vimeo video URL.",
            image="vimeo_video.jpg",
            slug="recipe-with-vimeo-video",
            content="Some content",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            video_url=valid_url
        )
        self.assertEqual(recipe.video_url, valid_url)

    # Test for cover picture upload path
    def test_cover_picture_upload_path(self):
        file = SimpleUploadedFile("test_cover.jpg", b"image_data")
        recipe = Recipe.objects.create(
            title="Recipe With Cover",
            excerpt="A recipe with an uploaded cover picture.",
            cover_picture=file,
            slug="recipe-with-cover",
            content="Recipe content goes here.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        self.assertTrue(recipe.cover_picture.name.startswith("recipe/"))

    # Test for empty cover picture
    def test_empty_cover_picture(self):
        recipe = Recipe.objects.create(
            title="Recipe Without Cover",
            excerpt="A recipe without a cover picture.",
            slug="recipe-without-cover",
            content="Recipe content goes here.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            cover_picture=None,  # No cover picture specified
        )
        self.assertIsNone(recipe.cover_picture.name if recipe.cover_picture else None)  # Check if the file is empty




