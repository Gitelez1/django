from django.urls import path
from . import views

urlpatterns = [
    path('process_money/<str:location>/', views.process_money, name='process_money'),
    path('some-path/', views.index6, name='index6'),
]