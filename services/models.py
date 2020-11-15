from django.db import models


# Create your models here.
class Services(models.Model):
    class Meta:
        verbose_name_plural = 'Наши услуги'

    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='services', blank=True)
    price = models.IntegerField(verbose_name='Стоимость')
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title
