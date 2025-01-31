from django.test import TestCase
from django.core.exceptions import ValidationError
from portfolio.models.tag import Tag

class TagModelTest(TestCase):

    def test_create_tag(self):
        # Test creating a valid Recipe instance
        tag = Tag.objects.create(caption="premium")
        # Assert the recipe's title and slug match the expected values
        self.assertEqual(tag.caption, "premium")

    def test_max_length_constraints(self):
        # Test max length constraints for fields
        tag = Tag(
            caption="T" * 31,  # Exceed max length of 81 for title
        )
        # Assert a ValidationError is raised for the exceeded length fields
        with self.assertRaises(ValidationError):
            tag.full_clean()

    def test_string_representation(self):
        # Test the __str__ method of the Recipe model
        tag = Tag(caption="premium")
        self.assertEqual(str(tag), "premium")
