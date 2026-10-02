from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "add products"

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name="Автотовары")

        autoparts = [
            {
                "name": "Зарядное устройство",
                "description": "Зарядное устройство для аккумулятора 12/24v",
                "price": 3199.00,
                "category": category,
            },
            {
                "name": "Набор для детейлинга",
                "description": "Набор от GRASS с Буруновым",
                "price": 2999.00,
                "category": category,
            },
            {
                "name": "Полироль",
                "description": "Полироль для кузова санкционная польская",
                "price": 1045.00,
                "category": category,
            },
            {
                "name": "Органайзер",
                "description": "Органайзер в башажник автомобиля",
                "price": 1979.00,
                "category": category,
            },
        ]

        for item in autoparts:
            product, created = Product.objects.get_or_create(**item)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added student: {product.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product: {product.name} already exists")
                )
