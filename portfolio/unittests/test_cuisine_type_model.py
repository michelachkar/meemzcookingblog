from django.test import TestCase
from django.core.exceptions import ValidationError
from portfolio.models.cuisine_type import CuisineType

class CuisineTypeModelTest(TestCase):

    def test_create_cuisine_type(self):
        # Test creating a valid Recipe instance
        cuisine_type = CuisineType.objects.create(name="Italian")
        # Assert the recipe's title and slug match the expected values
        self.assertEqual(cuisine_type.name, "Italian")

    def test_max_length_constraints(self):
        # Test max length constraints for fields
        cuisine_type = CuisineType(
            name="T" * 81,  # Exceed max length of 81 for title
        )
        # Assert a ValidationError is raised for the exceeded length fields
        with self.assertRaises(ValidationError):
            cuisine_type.full_clean()

    def test_string_representation(self):
        # Test the __str__ method of the Recipe model
        cuisine_type = CuisineType(name="Italian")
        self.assertEqual(str(cuisine_type), "Italian")
