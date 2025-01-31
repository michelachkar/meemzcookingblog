from django.shortcuts import render
from django.http import Http404, HttpResponseServerError
from datetime import date
from portfolio.models.recipe import Recipe
from portfolio.models.gallery_image import GalleryImage
from portfolio.models.dish_type import DishType
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

# Displays home page
def home(request):
    try:

        # Getting all recipes
        all_recipes = []
        dish_types = DishType.objects.all()
        for dish_type in dish_types:
            filtered_recipes = Recipe.objects.filter(dish_type_id=dish_type.id).order_by('-date')[:6]
            all_recipes.append((dish_type,filtered_recipes))

        #Getting Gallery Images
        gallery_images = GalleryImage.objects.all()[:8]
            
        #Getting content context
        context = {
            "intro_bloc": {
                "title": "Bienvenue dans mon blog",
                "subtitle": "Bonjour les foodies!",
                "description": "Je suis Meemz et j’ai 35 ans. Fan de chocolat, de fromage mais aussi de légumes, je partage ici avec vous des recettes faciles et délicieuses!",
                "cta": "À propos",
                "img": "portfolio/images/banners/1.png"
            },
            "service_bloc": {
                "title": "Private Dining and Events",
                "subtitle": "A Warm, Charming Atmosphere",
                "description": "Allow us to make your next special event extra special. We cater for all sized functions, ideal for your larger functions or an intimate gathering, our team can curate a menu to suit your taste.",
                "cta": "Mes Services",
                "img": "portfolio/images/banners/2.png"
            }
        }

        return render(request, 'portfolio/home.html', {'all_recipes': all_recipes, 'gallery_images':gallery_images, 'context': context})
    except DatabaseError as e:
        return HttpResponseServerError(f"Database error: {str(e)}")
    except Exception as e:
        return HttpResponseServerError(f"An unexpected error occurred: {str(e)}")
    

# Displays all recipes
def recipes(request):
    try:
        all_recipes = Recipe.objects.all().order_by('-date')
        return render(request, "./portfolio/recipes.html", {"recipes": all_recipes})
    except DatabaseError as e:
        return HttpResponseServerError(f"Database error: {str(e)}")
    except Exception as e:
        return HttpResponseServerError(f"An unexpected error occurred: {str(e)}")
    

# Displays recipes by dish type
def dish_type_recipes(request, dish_type_slug):
    try:
        dish_type = DishType.objects.get(slug=str(dish_type_slug))
        recipe_list = Recipe.objects.filter(dish_type_id=dish_type.id)
        return render(request, "./portfolio/dish_type_recipes.html", {
            "recipe_list": recipe_list,
            "dish_type": dish_type
            })
    except ObjectDoesNotExist:
        raise Http404()
    except DatabaseError as e:
        return HttpResponseServerError(f"Database error: {str(e)}")
    except Exception as e:
        return HttpResponseServerError(f"An unexpected error occurred: {str(e)}")



def recipe_detail(request, slug):
    try:
        recipe = Recipe.objects.get(slug=slug)
        return render(request, "./portfolio/recipe_detail.html", {
                "recipe": recipe,
                "tags": recipe.tags.all()
            })
    except ObjectDoesNotExist:
        raise Http404()
    except DatabaseError as e:
        return HttpResponseServerError(f"Database error: {str(e)}")
    except Exception as e:
        return HttpResponseServerError(f"An unexpected error occurred: {str(e)}")