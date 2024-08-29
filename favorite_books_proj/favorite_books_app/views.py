from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book
from .forms import BookForm

@login_required
def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'index.html', context)

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.uploaded_by = request.user
            book.save()
            book.users_who_like.add(request.user)
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    is_favorited = request.user in book.users_who_like.all()
    context = {
        'book': book,
        'is_favorited': is_favorited,
    }
    return render(request, 'book_detail.html', context)

@login_required
def favorite_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.user not in book.users_who_like.all():
        book.users_who_like.add(request.user)
    return redirect('book_detail', book_id=book_id)

@login_required
def unfavorite_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.user in book.users_who_like.all():
        book.users_who_like.remove(request.user)
    return redirect('book_detail', book_id=book_id)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
