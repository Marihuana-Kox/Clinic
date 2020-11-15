from django.shortcuts import render

# Create your views here.
from category.models import Category
from services.models import Services


def detail_category(request, slug):
    detail = Category.objects.get(slug=slug)
    servic = Services.objects.filter(category=detail)
    return render(request, 'category/detail_category.html', {'detail': detail, 'servic': servic,})
