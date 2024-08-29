from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('new/', views.register, name='new'),  # Handle /users/new with the same view as /register
    path('me/', views.index7, name='index7'),
]
