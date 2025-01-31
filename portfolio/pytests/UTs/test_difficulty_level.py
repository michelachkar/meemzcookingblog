from django.test import TestCase
from django.core.exceptions import ValidationError
from portfolio.models.difficulty_level import DifficultyLevel

class DifficultyLevelModelTest(TestCase):

    def test_create_difficulty_level(self):
        # Test creating a valid Recipe instance
        difficulty_level = DifficultyLevel.objects.create(name="Easy")
        # Assert the recipe's title and slug match the expected values
        self.assertEqual(difficulty_level.name, "Easy")

    def test_max_length_constraints(self):
        # Test max length constraints for fields
        difficulty_level = DifficultyLevel(
            name="T" * 81,  # Exceed max length of 81 for title
        )
        # Assert a ValidationError is raised for the exceeded length fields
        with self.assertRaises(ValidationError):
            difficulty_level.full_clean()

    def test_string_representation(self):
        # Test the __str__ method of the Recipe model
        difficulty_level = DifficultyLevel(name="Easy")
        self.assertEqual(str(difficulty_level), "Easy")
