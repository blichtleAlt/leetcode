# pages/urls.py
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:post_id>/', detail, name='detail'),
]