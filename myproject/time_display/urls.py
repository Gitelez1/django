from django.urls import path
from . import views

urlpatterns = [
    path('display/', views.index1, name='index1'),
    path('getpost/', views.index2, name='index2'),
]
