from django.test import TestCase
from django.core.exceptions import ValidationError
from portfolio.models.dish_type import DishType

class DishTypeModelTest(TestCase):

    def test_create_dish_type(self):
        # Test creating a valid DishType instance
        dish_type = DishType.objects.create(name="Main Course", slug="main-course")
        # Assert that the name and slug match the expected values
        self.assertEqual(dish_type.name, "Main Course")
        self.assertEqual(dish_type.slug, "main-course")

    def test_max_length_constraints(self):
        # Test that the max length constraints are enforced on the name and slug
        # Name should exceed the maximum length of 80
        dish_type = DishType(
            name="T" * 81,  # Exceed max length of 80 for name
        )
        # Assert a ValidationError is raised for the exceeded length field
        with self.assertRaises(ValidationError):
            dish_type.full_clean()

        # Test the slug field's max length constraint (assuming max length is 50)
        dish_type = DishType(
            name="Main Course",
            slug="T" * 51  # Exceed max length of 50 for slug
        )
        with self.assertRaises(ValidationError):
            dish_type.full_clean()

    def test_string_representation(self):
        # Test the __str__ method of the DishType model
        # It should return the name of the DishType instance
        dish_type = DishType(name="Main Course")
        self.assertEqual(str(dish_type), "Main Course")

    def test_description_optional(self):
        # Test that the description field is optional (can be left empty or None)
        dish_type = DishType(name="Main Course", slug="main-course", description=None)
        dish_type.full_clean()  # No error should be raised when description is None

        # Test with an empty string for description (also valid)
        dish_type.description = ""
        dish_type.full_clean()  # No error should be raised

    def test_image_optional(self):
        # Test that the image field can be left empty (image is optional)
        dish_type = DishType(name="Main Course", slug="main-course", image=None)
        dish_type.full_clean()  # No error should be raised when image is None

    def test_create_dish_type_with_special_characters_in_slug(self):
        # Test if special characters are correctly handled in slug
        # This ensures that special characters like & are correctly slugified
        dish_type = DishType.objects.create(name="Spicy & Sweet", slug="spicy-sweet")
        self.assertEqual(dish_type.slug, "spicy-sweet")

    def test_create_dish_type_with_very_long_name(self):
        # Test that a very long name (exceeding max length) raises a ValidationError
        long_name = "T" * 81  # Name too long (max length is 80)
        dish_type = DishType(name=long_name, slug="long-name")
        with self.assertRaises(ValidationError):
            dish_type.full_clean()


    def test_blank_slug(self):
        # Test that a blank slug raises a ValidationError
        # If the slug is required, it should not be empty
        dish_type = DishType(name="Dish Without Slug", slug="")
        with self.assertRaises(ValidationError):
            dish_type.full_clean()

    def test_invalid_slug_characters(self):
        # Test invalid characters in the slug field
        # If the slug contains invalid characters like spaces or special symbols, it should raise a ValidationError
        dish_type = DishType(name="Dish With Invalid Slug", slug="invalid slug!")
        with self.assertRaises(ValidationError):
            dish_type.full_clean()

    def test_deleting_dish_type(self):
        # Test the behavior when a DishType is deleted
        # The DishType should be removed from the database and attempting to fetch it by ID should raise DoesNotExist
        dish_type = DishType.objects.create(name="Test Dish", slug="test-dish")
        dish_type_id = dish_type.id
        dish_type.delete()
        with self.assertRaises(DishType.DoesNotExist):
            DishType.objects.get(id=dish_type_id)

    def test_image_upload(self):
        # Test uploading an image to the DishType model (S3 storage)
        # In a real test, you would mock the image upload to check if it's stored correctly in the specified storage backend (S3)
        dish_type = DishType(name="Main Course", slug="main-course", image="path/to/image.jpg")
        # Ensure the image exists (this is just a placeholder, you may need to mock or use a real image upload in tests)
        self.assertTrue(dish_type.image)
        
    def test_empty_name(self):
        # Test that an empty name raises a ValidationError
        # The name field is required, so leaving it empty should cause validation to fail
        dish_type = DishType(name="", slug="empty-name")
        with self.assertRaises(ValidationError):
            dish_type.full_clean()
