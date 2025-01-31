from django.db import models
from django.core.validators import URLValidator
from .cuisine_type import CuisineType
from .difficulty_level import DifficultyLevel
from .event_type import EventType
from .dish_type import DishType
from .main_ingredient import MainIngredient
from .tag import Tag
from django_ckeditor_5.fields import CKEditor5Field
from storages.backends.s3boto3 import S3Boto3Storage


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(
        max_length=150, 
        verbose_name="Recipe Title", 
        help_text="Enter the title of the recipe."
    )

    excerpt = models.CharField(
        max_length=200, 
        verbose_name="Short Description", 
        help_text="A brief summary of the recipe."
    )

    video_url = models.URLField(
        max_length=255,
        verbose_name="YouTube Video",
        help_text="Paste a link to a YouTube video for this recipe.",
        validators=[URLValidator()],
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to="recipe",
        storage=S3Boto3Storage(),
        verbose_name="Recipe Image",
        help_text="Upload an image for this recipe.",
        null=True, 
        blank=True
    )

    date = models.DateField(
        auto_now=True, 
        verbose_name="Last Updated"
    )

    slug = models.SlugField(
        unique=True, 
        db_index=True, 
        verbose_name="URL Slug",
        help_text="A unique slug for the recipe."
    )

    content = CKEditor5Field(
        config_name="default",
        verbose_name="Recipe Instructions",
        help_text="Provide step-by-step instructions for the recipe.",
        null=True, 
        blank=True
    )

    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.PROTECT,
        related_name="recipes",
        verbose_name="Dish Type",
        help_text="Select the type of dish for this recipe."
    )

    main_ingredient = models.ForeignKey(
        MainIngredient,
        on_delete=models.PROTECT,
        related_name="recipes",
        verbose_name="Main Ingredient",
        help_text="Select the primary ingredient of this recipe."
    )

    cuisine_type = models.ForeignKey(
        CuisineType,
        on_delete=models.PROTECT,
        related_name="recipes",
        verbose_name="Cuisine Type",
        help_text="Choose the cuisine style of this recipe."
    )

    difficulty_level = models.ForeignKey(
        DifficultyLevel,
        on_delete=models.PROTECT,
        related_name="recipes",
        verbose_name="Difficulty Level",
        help_text="Select the difficulty level for preparing this recipe."
    )

    event_type = models.ForeignKey(
        EventType,
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        related_name="recipes",
        verbose_name="Event Type",
        help_text="Optionally, select an event type this recipe is suitable for."
    )

    tags = models.ManyToManyField(
        Tag, 
        related_name="recipes",
        blank=True,
        verbose_name="Tags",
        help_text="Select tags to categorize this recipe."
    )


    def __str__(self):
        return self.title
