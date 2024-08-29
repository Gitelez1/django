from django.urls import path
from . import views

urlpatterns = [
    path('in/', views.index9, name='index9'),
    path('dojos/create/', views.create_dojo, name='create_dojo'),
    path('ninjas/create/', views.create_ninja, name='create_ninja'),
    path('dojos/delete/<int:dojo_id>/', views.delete_dojo, name='delete_dojo'),
]
