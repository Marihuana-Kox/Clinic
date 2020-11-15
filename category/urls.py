from django.urls import path

from .views import *

urlpatterns = [
    path('<slug:slug>/', detail_category, name='category'),
]