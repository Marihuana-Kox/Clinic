from django.db import models

# Create your models here.
class Specialists(models.Model):
    objects = None

    class Meta:
        verbose_name_plural = 'Персонал'

    name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Имя специалиста')
    image = models.ImageField(upload_to='specialists/', blank=True)
    description = models.CharField(max_length=255, verbose_name='Должность и звание')

    def __str__(self):
        return self.name