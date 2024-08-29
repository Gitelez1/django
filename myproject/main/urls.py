from django.urls import path
from . import views

urlpatterns = [
    path('one/', views.root_view, name='root'),
    path('destroy_session/', views.destroy_session, name='destroy_session'),
    path('increment_counter/<int:amount>/', views.increment_counter, name='increment_counter'),
]
