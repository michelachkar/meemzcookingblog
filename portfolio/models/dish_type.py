from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

# Create your models here.

class DishType(models.Model):
    name = models.CharField(max_length=80)

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Description",
        help_text="A brief description of the dish type."
    )

    image=models.ImageField(
        storage=S3Boto3Storage(),
        upload_to="dish_types",
        verbose_name="Dish Type Image",
        help_text="Upload an image for the dish type.",
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        unique=True, 
        db_index=True, 
        null=True,
        verbose_name="URL Slug",
        help_text="A unique slug for the dish type."
    )

    def __str__(self):
        return self.name