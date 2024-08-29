from django.shortcuts import render

from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse

def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs 1")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog 2")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder to display blog number {number} 3")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number} 4")

def destroy(request, number):
    return redirect('/blogs')

def blogs_json(request):
    data = {
        "title": "Sample Blog Title",
        "content": "Sample Blog Content"
    }
    return JsonResponse(data)

