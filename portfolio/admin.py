from django.contrib import admin
from portfolio.models.cuisine_type import CuisineType
from portfolio.models.difficulty_level import DifficultyLevel
from portfolio.models.dish_type import DishType
from portfolio.models.event_type import EventType
from portfolio.models.main_ingredient import MainIngredient
from portfolio.models.recipe import Recipe
from portfolio.models.gallery_image import GalleryImage
from portfolio.models.slide import Slide
from portfolio.models.tag import Tag
from portfolio.models.recipe_image import RecipeImage
from portfolio.models.recipe_ingredient import RecipeIngredient
from django_ckeditor_5.widgets import CKEditor5Widget
from django.db import models

# Register your models here.

class RecipeImageInline(admin.TabularInline):  
    model = RecipeImage
    extra = 1  # Number of empty image slots

# Inline model for ingredients
class RecipeIngredientInline(admin.TabularInline):  # You can use StackedInline for a different layout
    model = RecipeIngredient
    extra = 1  # Number of empty ingredient forms shown by default
    

class RecipeAdmin(admin.ModelAdmin):
    list_filter = ("date", "dish_type", "main_ingredient", "cuisine_type", "difficulty_level", "event_type", "tags")
    list_display = ("title", "date", "dish_type", "main_ingredient", "cuisine_type", "difficulty_level", "event_type")
    prepopulated_fields = {"slug" : ("title",)}
    inlines = [RecipeImageInline, RecipeIngredientInline]
    formfield_overrides = {
        models.TextField: {"widget": CKEditor5Widget(config_name="default")},
    }

class DishTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("name",)}


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(CuisineType)
admin.site.register(DifficultyLevel)
admin.site.register(DishType, DishTypeAdmin)
admin.site.register(EventType)
admin.site.register(MainIngredient)
admin.site.register(Tag)
admin.site.register(GalleryImage)
admin.site.register(Slide)
admin.site.register(RecipeIngredient)


