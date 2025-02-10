from django.test import TestCase
from django.urls import reverse
from django.core.paginator import Paginator
from portfolio.models.recipe import Recipe
from portfolio.models.dish_type import DishType
from portfolio.models.cuisine_type import CuisineType
from portfolio.models.difficulty_level import DifficultyLevel
from portfolio.models.main_ingredient import MainIngredient
from portfolio.models.event_type import EventType
from portfolio.models.tag import Tag
from datetime import date

class RecipeSearchViewTests(TestCase):
    @classmethod
    def setUpTestData(self):
        # Creating related objects
        self.dish_type = DishType.objects.create(name="Dessert")
        self.cuisine_type = CuisineType.objects.create(name="French")
        self.difficulty_level = DifficultyLevel.objects.create(name="Easy")
        self.main_ingredient = MainIngredient.objects.create(name="Chocolate")
        self.event_type = EventType.objects.create(name="Birthday")
        self.tag = Tag.objects.create(caption="Sweet")
        
        # Creating recipes
        recipe = Recipe.objects.create(
            title=f"Chocolate Cake",
            excerpt="A delicious chocolate cake recipe.",
            video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            slug=f"chocolate-cake-133",
            dish_type=self.dish_type,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            main_ingredient=self.main_ingredient,
            event_type=self.event_type,
            date=date.today()
        )
        # Creating recipes
        recipe = Recipe.objects.create(
            title=f"Vanilla Ice Cream",
            excerpt="A delicious chocolate cake recipe.",
            video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            slug=f"chocolate-cake-233",
            dish_type=self.dish_type,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            main_ingredient=self.main_ingredient,
            event_type=self.event_type,
            date=date.today()
        )
        # Creating recipes
        recipe = Recipe.objects.create(
            title=f"Strawberry Tart",
            excerpt="A delicious chocolate cake recipe.",
            video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            slug=f"chocolate-cake-333",
            dish_type=self.dish_type,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            main_ingredient=self.main_ingredient,
            event_type=self.event_type,
            date=date.today()
        )
        # Creating recipes
        recipe = Recipe.objects.create(
            title=f"Apple Pie",
            excerpt="A delicious chocolate cake recipe.",
            video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            slug=f"chocolate-cake-433",
            dish_type=self.dish_type,
            cuisine_type=self.cuisine_type,
            difficulty_level=self.difficulty_level,
            main_ingredient=self.main_ingredient,
            event_type=self.event_type,
            date=date.today()
        )
        
        # Create more recipes to test pagination
        for i in range(20):
            # Creating recipes
            recipe = Recipe.objects.create(
                title=f"Recipe {i}",
                excerpt="A delicious chocolate cake recipe.",
                video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                slug=f"chocolate-cake-{i}",
                dish_type=self.dish_type,
                cuisine_type=self.cuisine_type,
                difficulty_level=self.difficulty_level,
                main_ingredient=self.main_ingredient,
                event_type=self.event_type,
                date=date.today()
            )
    
    def test_search_view_renders_correct_template(self):
        response = self.client.get(reverse('recipe_search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './portfolio/search_results.html')
    
    def test_search_with_valid_query(self):
        response = self.client.get(reverse('recipe_search'), {'search': 'Chocolate'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chocolate Cake")
        self.assertNotContains(response, "Vanilla Ice Cream")
    
    def test_search_with_partial_query(self):
        response = self.client.get(reverse('recipe_search'), {'search': 'Cake'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chocolate Cake")
    
    def test_search_with_no_results(self):
        response = self.client.get(reverse('recipe_search'), {'search': 'NonExistentRecipe'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aucune recette trouvée")  # Assuming this is shown in the template
    
    def test_search_with_empty_query(self):
        response = self.client.get(reverse('recipe_search'), {'search': ''})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['results']), 0)
    
    def test_pagination_first_page(self):
        response = self.client.get(reverse('recipe_search'), {'search': 'Recipe', 'page': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['results']), 12)  # 12 per page
    
    def test_pagination_second_page(self):
        response = self.client.get(reverse('recipe_search'), {'search': 'Recipe', 'page': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['results']), 8)  # Remaining results on page 2
    
    def test_pagination_invalid_page(self):
        response = self.client.get(reverse('recipe_search'), {'search': 'Recipe', 'page': 'invalid'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['results'].number, 1)  # Defaults to first page
    
    def test_pagination_out_of_range_page(self):
        response = self.client.get(reverse('recipe_search'), {'search': 'Recipe', 'page': 100})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['results'].number, Paginator(Recipe.objects.all(), 12).num_pages)  # Last page
