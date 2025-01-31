from django.test import TestCase
from django.core.exceptions import ValidationError
from portfolio.models.dish_type import DishType

class DishTypeModelTest(TestCase):

    def test_create_dish_type(self):
        # Test creating a valid Recipe instance
        dish_type = DishType.objects.create(name="Main Course")
        # Assert the recipe's title and slug match the expected values
        self.assertEqual(dish_type.name, "Main Course")

    def test_max_length_constraints(self):
        # Test max length constraints for fields
        dish_type = DishType(
            name="T" * 81,  # Exceed max length of 81 for title
        )
        # Assert a ValidationError is raised for the exceeded length fields
        with self.assertRaises(ValidationError):
            dish_type.full_clean()

    def test_string_representation(self):
        # Test the __str__ method of the Recipe model
        dish_type = DishType(name="Main Course")
        self.assertEqual(str(dish_type), "Main Course")
