from django.contrib import admin

# Register your models here.
from services.models import Services


class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'description', 'image', 'price')


admin.site.register(Services, ServicesAdmin)
