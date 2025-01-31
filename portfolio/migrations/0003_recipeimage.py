# Generated by Django 5.1.5 on 2025-01-26 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0002_recipe_video_url_alter_recipe_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecipeImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="Upload additional images for this recipe.",
                        upload_to="recipe_gallery/",
                        verbose_name="Recipe Gallery Image",
                    ),
                ),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="portfolio.recipe",
                    ),
                ),
            ],
        ),
    ]
