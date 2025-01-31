from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage


class Slide(models.Model):
    
    title=models.CharField(
        max_length=150,
    )

    subtitle=models.CharField(
        max_length=150,
    )

    paragraph=models.CharField(
        max_length=150,
    )

    cta_1_text=models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    cta_1_link=models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    cta_2_text=models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    cta_2_link=models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to="slider",
        storage=S3Boto3Storage(),
        verbose_name="Slide Image",
        help_text="Upload Image to the slider."
    )

    alt = models.CharField(
        max_length=150,
        null=True, 
        blank=True
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Slider for {self.title}"

