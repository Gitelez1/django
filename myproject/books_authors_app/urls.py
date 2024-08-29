from django.urls import path
from . import views

urlpatterns = [
    path('autor/', views.index10, name='index10'),  # Home page showing books and authors
    path('books/', views.book_list, name='book_list'),  # List all books
    path('authors/', views.author_list, name='author_list'),  # List all authors
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),  # Detail view for a specific book
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),  # Detail view for a specific author
    path('create/book/', views.create_book, name='create_book'),
    path('create/author/', views.create_author, name='create_author'),
    path('book/<int:book_id>/', views.book_detail1, name='book_detail1'),
    path('author/<int:author_id>/', views.author_detail1, name='author_detail1'),
]
