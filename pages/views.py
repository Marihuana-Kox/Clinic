from django.shortcuts import render

# Create your views here.
# def page_index(request):
#     return render(request, 'pages/index.html')
from django.template.context_processors import request

from pages.models import Pages
from services.models import Services
from specialists.models import Specialists


def index_page(request):
    page = Pages.objects.get(slug='index')
    service = Services.objects.all()
    persons = Specialists.objects.all()
    return render(request, 'pages/index.html', {'page': page, 'persons': persons, 'service': service})


def detail_page(request, slug):
    page = Pages.objects.get(slug=slug)
    return render(request, 'pages/index.html', {'page': page, })