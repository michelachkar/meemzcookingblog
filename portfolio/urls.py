from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("recettes", views.recipes, name="recipes"),
    path("recettes-de-<slug:dish_type_slug>", views.dish_type_recipes, name="recipes-dish-type"),
    path("recettes/<slug:slug>", views.recipe_detail, name="recipe_detail"),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("services/<slug:slug>", views.service_detail, name="service_detail"),
]