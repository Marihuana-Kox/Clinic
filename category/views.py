from django.shortcuts import render

# Create your views here.
from category.models import Category


def detail_category(request, slug):
    detail = Category.objects.get(slug=slug)
    return render(request, 'category/detail_category.html', {'detail': detail,})
