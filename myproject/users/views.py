from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index7(request):
    # Example list of users
    users = [{'id': 1, 'username': 'john_doe'}, {'id': 2, 'username': 'jane_smith'}]  # Replace with actual user data
    return render(request, 'index7.html', {'users': users})

def register(request):
    return HttpResponse("placeholder for users to create a new user record")

def login(request):
    return HttpResponse("placeholder for users to log in")

def index(request):
    return HttpResponse("placeholder to later display all the list of users")
