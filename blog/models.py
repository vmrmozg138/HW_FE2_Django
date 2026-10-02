from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок"
    )
    content = models.TextField(
        verbose_name="Содержимое"
    )
    preview_image = models.ImageField(
        upload_to='blog/previews/',
        blank=True,
        null=True,
        verbose_name="Превью (изображение)"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Признак публикации"
    )
    views = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров"
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']  # новые посты первыми

    def __str__(self):
        return self.title
