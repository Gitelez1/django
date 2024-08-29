from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author

def index10(request):
    return render(request, 'index10.html')

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book_list.html', context)

def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'author_list.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {'book': book, 'authors': book.authors.all()}
    return render(request, 'book_detail.html', context)

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    context = {'author': author, 'books': author.books.all()}
    return render(request, 'author_detail.html', context)

def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        book = Book.objects.create(title=title)
        return redirect('create_book')  # Redirect after creation
    books = Book.objects.all()
    return render(request, 'create_book.html', {'books': books})


def create_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = Author.objects.create(name=name)
        return redirect('create_author')  # Redirect after creation
    authors = Author.objects.all()
    return render(request, 'create_author.html', {'authors': authors})

def book_detail1(request, book_id):
    book = Book.objects.get(id=book_id)
    authors = Author.objects.exclude(books=book)  # Authors not yet associated with this book
    if request.method == 'POST':
        author_id = request.POST.get('author')
        book.authors.add(author_id)  # Associate author with book
        return redirect('book_detail1', book_id=book_id)
    return render(request, 'book_detail.html', {'book': book, 'authors': authors})

def author_detail1(request, author_id):
    author = Author.objects.get(id=author_id)
    books = Book.objects.exclude(authors=author)  # Books not yet associated with this author
    if request.method == 'POST':
        book_id = request.POST.get('book')
        author.books.add(book_id)  # Associate book with author
        return redirect('author_detail', author_id=author_id)
    return render(request, 'author_detail.html', {'author': author, 'books': books})
