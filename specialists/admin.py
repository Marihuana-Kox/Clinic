from django.contrib import admin

# Register your models here.
from specialists.models import Specialists


class SpecialistsAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "description")


admin.site.register(Specialists, SpecialistsAdmin)
