# pages/urls.py
from django.urls import path

from .views import *

urlpatterns = [
    path('', homePageView, name='home'),
    path('create', createPageView, name='create'),
    path('user', userPageView, name='user')
]