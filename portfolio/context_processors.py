from portfolio.models.dish_type import DishType
from django.core.cache import cache
from django.conf import settings


def menu_dish_types(request):
    dish_types = cache.get("menu_dish_types")

    if dish_types is None:  # If not cached, query DB
        dish_types = DishType.objects.all()
        cache.set("menu_dish_types", dish_types, timeout=3600)  # Cache for 1 hour

    return {'menu_dish_types': dish_types}

def aws_settings(request):
    return {
        'AWS_S3_CUSTOM_DOMAIN': settings.AWS_S3_CUSTOM_DOMAIN
    }