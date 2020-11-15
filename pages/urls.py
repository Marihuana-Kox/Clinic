from django.urls import path

from . import views
from .views import *

urlpatterns = [
    # path('', page_index, name='index'),
    path('', index_page, name='index'),
    path('<slug:slug>/', detail_page, name='pages'),
]