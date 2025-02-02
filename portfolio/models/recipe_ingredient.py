from django.db import models
from .recipe import Recipe

# Create your models here.

class RecipeIngredient(models.Model):
    name = models.CharField(max_length=80)

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients",
        verbose_name="Recipe",
        help_text="Select the recipe associated to this ingredient."
    )

    def __str__(self):
        return self.name