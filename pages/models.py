from django.db import models

# Create your models here.
class Pages(models.Model):
    objects = None

    class Meta:
        verbose_name_plural = 'Страницы'

    slug = models.SlugField(max_length=30, unique=True)
    image = models.ImageField(upload_to='page/', blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='Название страницы')
    body =models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.slug
