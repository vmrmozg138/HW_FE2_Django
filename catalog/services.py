from django.core.cache import cache

from config.settings import CACHE_ENABLED

from .models import Category, Product


def get_products_from_cache():
    if not CACHE_ENABLED:
        products = Product.objects.all()
        return products
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


class ProductService:

    @staticmethod
    def get_products_by_category(category):
        return Product.objects.filter(category=category).order_by("id")
