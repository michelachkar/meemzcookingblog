from django.shortcuts import render
from django.http import Http404, HttpResponseServerError
from portfolio.models.recipe import Recipe
from portfolio.models.gallery_image import GalleryImage
from portfolio.models.slide import Slide
from portfolio.models.dish_type import DishType
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.conf import settings
from portfolio.forms.contact_form import ContactForm
from django.views.generic.edit import FormView
import smtplib

# Create your views here.

# Displays home page


def home(request):
    try:
        # Getting all recipes
        all_recipes = []
        dish_types = DishType.objects.all()
        for dish_type in dish_types:
            filtered_recipes = Recipe.objects.filter(
                dish_type_id=dish_type.id).order_by('-date')[:6]
            all_recipes.append((dish_type, filtered_recipes))

        # Getting content context
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

        return render(request, 'portfolio/home.html', {
            'all_recipes': all_recipes,
            'gallery_images': GalleryImage.objects.all()[:8],
            'slides': Slide.objects.all(),
            'context': context
        })
    except DatabaseError as e:
        return HttpResponseServerError(f"Database error: {str(e)}")
    except Exception as e:
        return HttpResponseServerError(f"An unexpected error occurred: {str(e)}")


# Displays all recipes
def recipes(request):
    try:
        return render(request, "./portfolio/recipes.html", {"dish_types": DishType.objects.all()})
    except DatabaseError as e:
        return HttpResponseServerError(f"Database error: {str(e)}")
    except Exception as e:
        return HttpResponseServerError(f"An unexpected error occurred: {str(e)}")


# Displays recipes by dish type
def dish_type_recipes(request, dish_type_slug):
    try:
        dish_type = DishType.objects.get(slug=str(dish_type_slug))
        recipe_list = Recipe.objects.filter(dish_type_id=dish_type.id).order_by('-date')
        paginator = Paginator(recipe_list, 12)  # Show 12 recipes per page
        page = request.GET.get('page')

        try:
            recipes = paginator.page(page)
        except PageNotAnInteger:
            recipes = paginator.page(1)
        except EmptyPage:
            recipes = paginator.page(paginator.num_pages)

        return render(request, "./portfolio/dish_type_recipes.html", {
            "recipe_list": recipes,
            "dish_type": dish_type
        })

    except ObjectDoesNotExist:
        raise Http404()
    except DatabaseError as e:
        return HttpResponseServerError(f"Database error: {str(e)}")
    except Exception as e:
        return HttpResponseServerError(f"An unexpected error occurred: {str(e)}")

# Displays recipe details
def recipe_detail(request, slug):
    try:
        #Get recipe
        recipe = Recipe.objects.get(slug=slug)
        
        #Get similar recipes based on Dish Type of main recipe
        similar_recipes = Recipe.objects.filter(dish_type=recipe.dish_type).exclude(id=recipe.id).order_by('-date')[:2]

        return render(request, "./portfolio/recipe_detail.html", {
            "recipe": recipe,
            "ingredients": recipe.ingredients.all(),
            "tags": recipe.tags.all(),
            "similar_recipes": similar_recipes
        })
    except ObjectDoesNotExist:
        raise Http404()
    except DatabaseError as e:
        return HttpResponseServerError(f"Database error: {str(e)}")
    except Exception as e:
        return HttpResponseServerError(f"An unexpected error occurred: {str(e)}")
    

def service_detail(request, slug):
    service_templates = {
        'cours-de-cuisine': "portfolio/services/service_cours_de_cuisine.html",
        'team-building-cuisine': "portfolio/services/service_team_building_cuisine.html",
        'atelier-cuisine-enfants': "portfolio/services/service_atelier_cuisine_enfants.html"
    }

    template = service_templates.get(slug)
    if not template:
        raise Http404()
    
    return render(request, template)

def about(request):
    return render(request, "./portfolio/about.html")


class ContactFormView(FormView):
    template_name = './portfolio/contact.html'  # your template name
    form_class = ContactForm  # the form class
    success_url = '/'  # Redirect to home or any page after success

    def form_valid(self, form):
        # Get the form data
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']
        service = form.cleaned_data['service']

        # Prepare email content
        subject = f"Message from {first_name} {last_name}"
        body = f"Name: {first_name} {last_name}\nEmail: {email}\nPhone: {phone}\n\nService: {service}\n\nMessage:\n{message}"
        from_email = settings.DEFAULT_FROM_EMAIL  # Email configured in settings
        recipient_list = ['meeriamzouein@gmail.com']  # Replace with your actual recipient email

        # Send email and handle potential exceptions
        try:
            send_mail(subject, body, from_email, recipient_list)
        except Exception as e:
            # Optionally log the error or handle it
            print(f"Error sending email: {e}")
            # You can either handle the error gracefully here or re-raise it if needed
            raise

        # Call parent method to handle the redirect to success_url
        return super().form_valid(form)
    

    
    

