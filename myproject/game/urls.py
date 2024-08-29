from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_game, name='start_game'),
    path('guess/', views.guess_number, name='guess_number'),
    path('submit_name/', views.submit_name, name='submit_name'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
