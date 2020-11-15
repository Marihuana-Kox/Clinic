from django.contrib import admin

# Register your models here.
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'description', 'image', 'slug')


admin.site.register(Category, CategoryAdmin)
