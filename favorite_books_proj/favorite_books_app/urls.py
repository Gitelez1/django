from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_book/', views.add_book, name='add_book'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/favorite/', views.favorite_book, name='favorite_book'),
    path('book/<int:book_id>/unfavorite/', views.unfavorite_book, name='unfavorite_book'),
]
