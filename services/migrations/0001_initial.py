# Generated by Django 3.0 on 2020-11-12 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='services')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
