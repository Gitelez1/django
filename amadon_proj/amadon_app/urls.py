from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('amadon/buy', views.buy, name='buy'),
    path('amadon/checkout', views.checkout, name='checkout'),
]
