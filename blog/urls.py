# pages/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>/', detail, name='detail'),
    # path('post/<int:post_id>/comments', comments, name='comments'),
    path('signup/', AddUserView.as_view(), name='signup'),
    path('create/', create, name='create'),
    path('projects/', projects, name='projects'),
    path('about/', about, name='about'),
]
