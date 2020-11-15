from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Категории услуг'

    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='category/', blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title
