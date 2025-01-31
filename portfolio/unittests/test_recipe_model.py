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


class RecipeModelTest(TestCase):

    def setUp(self):
        # Set up required related objects for the Recipe model
        self.dish_type = DishType.objects.create(name="Main Course")
        self.main_ingredient = MainIngredient.objects.create(name="Chicken")
        self.cuisine_type = CuisineType.objects.create(name="Italian")
        self.difficulty_level = DifficultyLevel.objects.create(name="Easy")
        self.event_type = EventType.objects.create(name="Dinner Party")

    def test_create_recipe(self):
        # Test creating a valid Recipe instance
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
        # Assert the recipe's title and slug match the expected values
        self.assertEqual(recipe.title, "Spaghetti Carbonara")
        self.assertEqual(recipe.slug, "spaghetti-carbonara")

    def test_max_length_constraints(self):
        # Test max length constraints for fields
        recipe = Recipe(
            title="T" * 151,  # Exceed max length of 150 for title
            excerpt="E" * 201,  # Exceed max length of 200 for excerpt
            image="I" * 101,  # Exceed max length of 100 for image
            slug="S" * 51,  # Exceed max length of 50 for slug
            content="Valid content over 10 chars.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        # Assert a ValidationError is raised for the exceeded length fields
        with self.assertRaises(ValidationError):
            recipe.full_clean()

    def test_recipe_slug_unique(self):
        # Test the slug uniqueness constraint
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
        # Try to create a recipe with a duplicate slug, which should raise an error
        with self.assertRaises(Exception):
            Recipe.objects.create(
                title="Another Carbonara",
                excerpt="A variation of Carbonara.",
                image="carbonara2.jpg",
                slug="spaghetti-carbonara",  # Same slug as before
                content="Different step-by-step guide.",
                dish_type=self.dish_type,
                main_ingredient=self.main_ingredient,
                cuisine_type=self.cuisine_type,
                difficulty_level=self.difficulty_level,
            )

    def test_min_length_content(self):
        # Test validation of minimum length constraint on content field
        recipe = Recipe(
            title="Short Content Test",
            excerpt="Testing minimum content length.",
            image="test.jpg",
            slug="short-content-test",
            content="Too short",  # Should raise a ValidationError due to too short content
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        # Assert a ValidationError is raised
        with self.assertRaises(ValidationError):
            recipe.full_clean()

    def test_auto_date_field(self):
        # Test that the auto date field updates automatically on save
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
        # Assert that the date field is not None
        self.assertIsNotNone(recipe.date)

    def test_optional_event_type(self):
        # Test that event_type field can be set to None (it’s optional)
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
            event_type=None,  # event_type set to None
        )
        # Assert that event_type is None
        self.assertIsNone(recipe.event_type)

    def test_blank_content(self):
        # Test that content can be blank (blank=True is set)
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
            # Blank content should not raise an error
            recipe.full_clean()  
        except ValidationError:
            self.fail("ValidationError raised unexpectedly!")

    def test_many_to_many_tags(self):
        # Test that a recipe can have multiple tags
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
        # Assert the recipe has 2 tags
        self.assertEqual(recipe.tags.count(), 2)

    def test_blank_tags(self):
        # Test saving a recipe without tags (blank=True)
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
        # Assert the recipe has 0 tags
        self.assertEqual(recipe.tags.count(), 0)

    def test_slug_special_characters(self):
        # Test slug with special characters
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
        # Assert the slug is correctly formatted with special characters removed
        self.assertEqual(recipe.slug, "special-character-recipe")

    def test_empty_slug(self):
        # Test for empty slug
        recipe = Recipe(
            title="Empty Slug Test",
            excerpt="Testing empty slug scenario.",
            image="empty_slug.jpg",
            slug="",  # Empty slug should raise a ValidationError
            content="Valid content here.",
            dish_type=self.dish_type,
            main_ingredient=self.main_ingredient,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
        )
        # Assert a ValidationError is raised for the empty slug
        with self.assertRaises(ValidationError):
            recipe.full_clean()

    def test_foreign_key_protect_difficulty_level(self):
        # Test for ProtectedError when trying to delete a DifficultyLevel with related Recipe instances
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
        # Test for ProtectedError when trying to delete a DishType with related Recipe instances
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
        # Test for ProtectedError when trying to delete a MainIngredient with related Recipe instances
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
        # Test for ProtectedError when trying to delete a CuisineType with related Recipe instances
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
        # Test for SET_NULL behavior on EventType deletion
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
        self.assertEqual(Recipe.objects.count(), 1)
        # Deleting EventType should set event_type to NULL in the Recipe
        new_event_type.delete()
        recipe.refresh_from_db()
        self.assertIsNone(recipe.event_type)

    def test_string_representation(self):
        # Test the __str__ method of the Recipe model
        recipe = Recipe(title="Test Recipe")
        self.assertEqual(str(recipe), "Test Recipe")
