from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
import bcrypt

def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    errors = User.objects.validate_login(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    # Registration logic here
    return redirect('/wall/')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, "Please fill out both fields.")
            return redirect('/')

        user = User.objects.filter(email=email).first()

        if user and check_password(password, user.password):
            request.session['user_id'] = user.id
            return redirect('/wall/')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('/')
    return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')
