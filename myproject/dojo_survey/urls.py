from django.urls import path
from . import views

urlpatterns = [
    path('survey/', views.index4, name='index4'),
    path('form_post/', views.form_post, name='form_post'),
    path('result/', views.result, name='result'),
]
