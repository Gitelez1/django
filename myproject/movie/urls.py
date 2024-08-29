# movie/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('star', views.index, name='index'),  # Example pattern
]
