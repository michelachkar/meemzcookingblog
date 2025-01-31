from django.db import models

# Create your models here.

class DishType(models.Model):
    name = models.CharField(max_length=80)

    slug = models.SlugField(
        unique=True, 
        db_index=True, 
        null=True,
        verbose_name="URL Slug",
        help_text="A unique slug for the dish type."
    )

    def __str__(self):
        return self.name