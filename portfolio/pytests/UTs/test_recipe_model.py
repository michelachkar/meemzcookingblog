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
        # Set up required related objects for the Recipe model
        self.dish_type = DishType.objects.create(name="Main Course")
        self.main_ingredient = MainIngredient.objects.create(name="Chicken")
        self.cuisine_type = CuisineType.objects.create(name="Italian")
        self.difficulty_level = DifficultyLevel.objects.create(name="Easy")
        self.event_type = EventType.objects.create(name="Dinner Party")

    def test_create_recipe(self):
        """
        Test the creation of a recipe with all required fields. 
        Ensure that the title and slug are saved correctly.
        """
        recipe = Recipe.objects.create(
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
        self.assertEqual(recipe.title, "Spaghetti Carbonara")
        self.assertEqual(recipe.slug, "spaghetti-carbonara")

    def test_max_length_constraints(self):
        """
        Test that the model enforces maximum length constraints for title, excerpt, image, and slug.
        An error should be raised when the length exceeds the defined limit.
        """
        recipe = Recipe(
            title="T" * 151,  # Exceeds max length for title
            excerpt="E" * 201,  # Exceeds max length for excerpt
            image="I" * 101,  # Exceeds max length for image
            slug="S" * 51,  # Exceeds max length for slug
            content="Valid content over 10 chars.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        with self.assertRaises(ValidationError):
            recipe.full_clean()

    def test_recipe_slug_unique(self):
        """
        Test that the slug is unique. If two recipes have the same slug, 
        an error should be raised.
        """
        Recipe.objects.create(
            title="Spaghetti Carbonara",
            excerpt="A classic Italian pasta dish.",
            image="carbonara.jpg",
            slug="spaghetti-carbonara",
            content="Step-by-step guide.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        with self.assertRaises(Exception):
            Recipe.objects.create(
                title="Another Carbonara",
                excerpt="A variation of Carbonara.",
                image="carbonara2.jpg",
                slug="spaghetti-carbonara",  # Duplicate slug
                content="Different step-by-step guide.",
                dish_type=self.dish_type,
                main_ingredient=self.main_ingredient,
                cuisine_type=self.cuisine_type,
                difficulty_level=self.difficulty_level,
            )

    def test_auto_date_field(self):
        """
        Test that the `date` field is automatically set when creating a new recipe.
        """
        recipe = Recipe.objects.create(
            title="Auto Date Test",
            excerpt="Checking date field behavior.",
            image="date.jpg",
            slug="auto-date-test",
            content="Some valid content here.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        self.assertIsNotNone(recipe.date)

    def test_optional_event_type(self):
        """
        Test that the `event_type` field is optional. A recipe can be created without specifying an event type.
        """
        recipe = Recipe.objects.create(
            title="No Event Type",
            excerpt="This recipe has no event type.",
            image="noevent.jpg",
            slug="no-event-type",
            content="Just a simple recipe.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            event_type=None,  # No event type specified
        )
        self.assertIsNone(recipe.event_type)

    def test_blank_content(self):
        """
        Test that the content field can be left blank. It should not raise an error if blank.
        """
        recipe = Recipe.objects.create(
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
        try:
            recipe.full_clean()  # Should not raise ValidationError
        except ValidationError:
            self.fail("ValidationError raised unexpectedly!")

    def test_many_to_many_tags(self):
        """
        Test the many-to-many relationship between recipes and tags. Ensure that a recipe can have multiple tags.
        """
        recipe = Recipe.objects.create(
            title="Tagged Recipe",
            excerpt="Recipe with multiple tags.",
            image="tagged.jpg",
            slug="tagged-recipe",
            content="Some content here.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        tag1 = Tag.objects.create(caption="Quick")
        tag2 = Tag.objects.create(caption="Easy")
        recipe.tags.add(tag1, tag2)
        self.assertEqual(recipe.tags.count(), 2)

    def test_blank_tags(self):
        """
        Test that a recipe can be created without any tags, ensuring that tags are optional.
        """
        recipe = Recipe.objects.create(
            title="No Tags",
            excerpt="This recipe has no tags.",
            image="notags.jpg",
            slug="no-tags",
            content="Valid content here.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        self.assertEqual(recipe.tags.count(), 0)

    def test_slug_special_characters(self):
        """
        Test that special characters in the title are handled correctly in the slug field.
        The special characters should be sanitized.
        """
        recipe = Recipe.objects.create(
            title="Special @Character #Recipe",
            excerpt="Testing special characters in slug.",
            image="special_characters.jpg",
            slug=slugify("Special @Character #Recipe"),
            content="Some content with special characters.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        self.assertEqual(recipe.slug, "special-character-recipe")

    def test_empty_slug(self):
        """
        Test that an empty slug raises a validation error.
        The slug field should not be empty.
        """
        recipe = Recipe(
            title="Empty Slug Test",
            excerpt="Testing empty slug scenario.",
            image="empty_slug.jpg",
            slug="",  # Empty slug
            content="Valid content here.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        with self.assertRaises(ValidationError):
            recipe.full_clean()

    def test_foreign_key_protect_difficulty_level(self):
        """
        Test that difficulty levels are protected from deletion when referenced by a recipe.
        Deleting a referenced difficulty level should raise a ProtectedError.
        """
        new_difficulty = DifficultyLevel.objects.create(name="Very Difficult")
        recipe = Recipe.objects.create(
            title="Spaghetti Carbonara",
            excerpt="A classic Italian pasta dish with eggs, cheese, pancetta, and pepper.",
            image="carbonara.jpg",
            slug=slugify("Spaghetti Carbonara"),
            content="Cook pasta, fry pancetta, mix with eggs and cheese, combine and serve.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=new_difficulty,
            event_type=self.event_type,
        )
        self.assertEqual(Recipe.objects.count(), 1)
        with self.assertRaises(ProtectedError):
            new_difficulty.delete()

    def test_foreign_key_protect_dish_type(self):
        """
        Test that dish types are protected from deletion when referenced by a recipe.
        Deleting a referenced dish type should raise a ProtectedError.
        """
        new_dish_type = DishType.objects.create(name="Main Course")
        recipe = Recipe.objects.create(
            title="Spaghetti Carbonara",
            excerpt="A classic Italian pasta dish with eggs, cheese, pancetta, and pepper.",
            image="carbonara.jpg",
            slug=slugify("Spaghetti Carbonara"),
            content="Cook pasta, fry pancetta, mix with eggs and cheese, combine and serve.",
            dish_type=new_dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            event_type=self.event_type,
        )            
        self.assertEqual(Recipe.objects.count(), 1)
        with self.assertRaises(ProtectedError):
            new_dish_type.delete()

    def test_foreign_key_protect_main_ingredient(self):
        """
        Test that main ingredients are protected from deletion when referenced by a recipe.
        Deleting a referenced main ingredient should raise a ProtectedError.
        """
        new_main_ingredient = MainIngredient.objects.create(name="Chicken")
        recipe = Recipe.objects.create(
            title="Spaghetti Carbonara",
            excerpt="A classic Italian pasta dish with eggs, cheese, pancetta, and pepper.",
            image="carbonara.jpg",
            slug=slugify("Spaghetti Carbonara"),
            content="Cook pasta, fry pancetta, mix with eggs and cheese, combine and serve.",
            dish_type=self.dish_type,
            main_ingredient=new_main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            event_type=self.event_type,
        )
        self.assertEqual(Recipe.objects.count(), 1)
        with self.assertRaises(ProtectedError):
            new_main_ingredient.delete()

    def test_foreign_key_protect_cuisine_type(self):
        """
        Test that cuisine types are protected from deletion when referenced by a recipe.
        Deleting a referenced cuisine type should raise a ProtectedError.
        """
        new_cuisine_type = CuisineType.objects.create(name="Italian")
        recipe = Recipe.objects.create(
            title="Spaghetti Carbonara",
            excerpt="A classic Italian pasta dish with eggs, cheese, pancetta, and pepper.",
            image="carbonara.jpg",
            slug=slugify("Spaghetti Carbonara"),
            content="Cook pasta, fry pancetta, mix with eggs and cheese, combine and serve.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=new_cuisine_type,
            difficulty_level=self.difficulty_level,
            event_type=self.event_type,
        )
        self.assertEqual(Recipe.objects.count(), 1)
        with self.assertRaises(ProtectedError):
            new_cuisine_type.delete()

    def test_foreign_key_set_null_event_type(self):
        """
        Test that when an EventType is deleted, the related recipes have their event_type set to NULL.
        """
        new_event_type = EventType.objects.create(name="Coucou")
        recipe = Recipe.objects.create(
            title="Spaghetti Carbonara",
            excerpt="A classic Italian pasta dish with eggs, cheese, pancetta, and pepper.",
            image="carbonara.jpg",
            slug=slugify("Spaghetti Carbonara"),
            content="Cook pasta, fry pancetta, mix with eggs and cheese, combine and serve.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            event_type=new_event_type,
        )
        new_event_type.delete()
        recipe.refresh_from_db()
        self.assertIsNone(recipe.event_type)
    
    def test_image_upload_path(self):
        """
        Test that images are uploaded to the correct directory, following the recipe structure.
        """
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
        
    def test_video_url_validation(self):
        """
        Test that video URLs are validated. It should raise an error if the URL is invalid.
        """
        valid_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        recipe = Recipe.objects.create(
            title="Recipe With Video",
            excerpt="Recipe with a valid video URL.",
            image="video.jpg",
            slug="recipe-with-video",
            content="Some content",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            video_url=valid_url
        )
        self.assertEqual(recipe.video_url, valid_url)

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
