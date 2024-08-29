# login_app/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.validate_registration(request.POST)
        if User.objects.filter(email=request.POST['email']).exists():
            errors['email'] = "This email is already taken."
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=hashed_password,
                birthday=request.POST.get('birthday')
            )
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            return redirect('/success')

def login(request):
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = User.objects.get(email=request.POST['email'])
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            return redirect('/success')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'login_app/success.html')

def check_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email=email).exists()
    }
    return JsonResponse(data)

def logout(request):
    request.session.flush()
    return redirect('/')

