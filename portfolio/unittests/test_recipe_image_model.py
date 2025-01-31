from django.test import TestCase
from django.core.exceptions import ValidationError
from portfolio.models.recipe_image import RecipeImage
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

class RecipeImageModelTest(TestCase):

    def setUp(self):
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

    def test_create_recipe_image(self):
        # Test creating a valid RecipeImage instance
        recipe_image = RecipeImage.objects.create(
            recipe=self.recipe,
            alt="Test Image",
            image="path/to/image.jpg",  # Simulate an image path (this should ideally be mocked in real tests)
        )
        # Assert that the recipe image's alt text is correctly set
        self.assertEqual(recipe_image.alt, "Test Image")
        # Assert that the associated recipe is correctly set
        self.assertEqual(recipe_image.recipe, self.recipe)
        # Assert that the image field is correctly populated
        self.assertTrue(recipe_image.image)

    def test_alt_text_optional(self):
        # Test that the alt text can be left empty (optional field)
        recipe_image = RecipeImage.objects.create(
            recipe=self.recipe,
            image="path/to/image.jpg"
        )
        # Assert that the alt field is None when not provided
        self.assertIsNone(recipe_image.alt)

        # Test that setting the alt text to an empty string is valid
        recipe_image.alt = ""
        recipe_image.full_clean()  # No error should be raised when alt is empty

    def test_image_upload(self):
        # Test uploading an image (S3 storage)
        # In real tests, mocking the image upload is recommended to avoid hitting actual S3
        recipe_image = RecipeImage.objects.create(
            recipe=self.recipe,
            alt="Test Image",
            image="path/to/image.jpg"  # Simulated image path
        )
        # Assert that the image field is set properly
        self.assertTrue(recipe_image.image)

    def test_uploaded_at_auto_now_add(self):
        # Test that the 'uploaded_at' field is automatically set when a RecipeImage is created
        recipe_image = RecipeImage.objects.create(
            recipe=self.recipe,
            alt="Sample Image",
            image="path/to/image.jpg"
        )
        # Assert that the uploaded_at field is not None
        self.assertIsNotNone(recipe_image.uploaded_at)

    def test_max_length_constraints_for_alt(self):
        # Test max length constraint for alt text
        recipe_image = RecipeImage(
            alt="T" * 151,  # Exceed max length of 150 for alt text
            recipe=self.recipe,
            image="path/to/image.jpg",
        )
        # Assert that a ValidationError is raised for the exceeded length field
        with self.assertRaises(ValidationError):
            recipe_image.full_clean()

    def test_string_representation(self):
        # Test the __str__ method of the RecipeImage model
        recipe_image = RecipeImage(alt="Test Image", recipe=self.recipe, image="path/to/image.jpg")
        self.assertEqual(str(recipe_image), "Image for recipe Spaghetti Carbonara")

    def test_empty_alt_text(self):
        # Test that an empty alt text does not raise any validation errors
        recipe_image = RecipeImage(alt="", recipe=self.recipe, image="path/to/image.jpg")
        recipe_image.full_clean()  # No error should be raised for empty alt text

    def test_image_required(self):
        # Test that the image field is required (cannot be null)
        recipe_image = RecipeImage(alt="Test Image", recipe=self.recipe, image=None)
        # Assert that a ValidationError is raised when no image is provided
        with self.assertRaises(ValidationError):
            recipe_image.full_clean()

    def test_empty_image(self):
        # Test that an empty string for the image path raises a validation error
        recipe_image = RecipeImage(alt="Test Image", recipe=self.recipe, image="")
        # Assert that a ValidationError is raised when an empty image path is provided
        with self.assertRaises(ValidationError):
            recipe_image.full_clean()

    def test_recipe_foreign_key(self):
        # Test the relationship between RecipeImage and Recipe (ForeignKey)
        recipe_image = RecipeImage.objects.create(
            recipe=self.recipe,
            alt="Sample Image",
            image="path/to/image.jpg"
        )
        # Ensure the related recipe can be accessed from the RecipeImage instance
        self.assertEqual(recipe_image.recipe.title, "Spaghetti Carbonara")

    def test_deleting_recipe_image(self):
        # Test the behavior when a RecipeImage is deleted
        recipe_image = RecipeImage.objects.create(
            recipe=self.recipe,
            alt="Sample Image",
            image="path/to/image.jpg"
        )
        recipe_image_id = recipe_image.id
        # Delete the RecipeImage instance
        recipe_image.delete()
        # Ensure the RecipeImage instance is removed from the database
        with self.assertRaises(RecipeImage.DoesNotExist):
            RecipeImage.objects.get(id=recipe_image_id)
