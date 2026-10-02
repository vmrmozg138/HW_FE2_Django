from django.db import models

from users.models import CustomUser

# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name="Название категории"
    )
    description = models.TextField(blank=True, verbose_name="Описание категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(
        max_length=100, verbose_name="Название", help_text="Введите название продукта"
    )
    description = models.TextField(
        max_length=2000, verbose_name="Описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="catalog/images/",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото",
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за единицу",
        help_text="Введите цену",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(default=False)

    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец продукта",
        help_text="Укажите владельца продукта",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["price"]),
            models.Index(fields=["category", "price"]),
        ]
        permissions = [("can_unpublish_product", "Can unpublish product")]

    def __str__(self) -> str:
        return f"{self.name} ({self.category.name})"
