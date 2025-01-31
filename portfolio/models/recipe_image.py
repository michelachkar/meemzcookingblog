from django.db import models
from .recipe import Recipe
from storages.backends.s3boto3 import S3Boto3Storage


class RecipeImage(models.Model):

    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        related_name="images"
    )

    alt = models.CharField(
        max_length=150,
        null=True, 
        blank=True
    )

    image = models.ImageField(
        upload_to="recipe_images",
        storage=S3Boto3Storage(),
        verbose_name="Recipe Gallery Image",
        help_text="Upload additional images for this recipe."
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

