from django.test import TestCase
from django.core.exceptions import ValidationError
from portfolio.models.main_ingredient import MainIngredient

class MainIngredientModelTest(TestCase):

    def test_create_main_ingredient(self):
        # Test creating a valid Recipe instance
        main_ingredient = MainIngredient.objects.create(name="Chicken")
        # Assert the recipe's title and slug match the expected values
        self.assertEqual(main_ingredient.name, "Chicken")

    def test_max_length_constraints(self):
        # Test max length constraints for fields
        main_ingredient = MainIngredient(
            name="T" * 81,  # Exceed max length of 81 for title
        )
        # Assert a ValidationError is raised for the exceeded length fields
        with self.assertRaises(ValidationError):
            main_ingredient.full_clean()

    def test_string_representation(self):
        # Test the __str__ method of the Recipe model
        main_ingredient = MainIngredient(name="Chicken")
        self.assertEqual(str(main_ingredient), "Chicken")
