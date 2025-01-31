from django.test import TestCase
from django.core.exceptions import ValidationError
from portfolio.models.event_type import EventType

class EventTypeModelTest(TestCase):

    def test_create_event_type(self):
        # Test creating a valid Recipe instance
        event_type = EventType.objects.create(name="Dinner Party")
        # Assert the recipe's title and slug match the expected values
        self.assertEqual(event_type.name, "Dinner Party")

    def test_max_length_constraints(self):
        # Test max length constraints for fields
        event_type = EventType(
            name="T" * 81,  # Exceed max length of 81 for title
        )
        # Assert a ValidationError is raised for the exceeded length fields
        with self.assertRaises(ValidationError):
            event_type.full_clean()

    def test_string_representation(self):
        # Test the __str__ method of the Recipe model
        event_type = EventType(name="Dinner Party")
        self.assertEqual(str(event_type), "Dinner Party")
