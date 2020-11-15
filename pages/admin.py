from django.contrib import admin

# Register your models here.
from pages.models import Pages


class PagesAdmin(admin.ModelAdmin):
    list_display = ("pk", "slug", "title", "body")


admin.site.register(Pages, PagesAdmin)