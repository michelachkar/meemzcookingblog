from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

# Create your models here.

class GalleryImage(models.Model):

    alt = models.CharField(
        max_length=150,
        null=True, 
        blank=True
    )

    image = models.ImageField(
        storage=S3Boto3Storage(),
        verbose_name="Gallery Image",
        help_text="Upload additional images for the gallery."
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.alt}"

