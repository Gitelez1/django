from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index9(request):
    dojos = Dojo.objects.all()
    return render(request, 'index9.html', {'dojos': dojos})

def create_dojo(request):
    if request.method == 'POST':
        Dojo.objects.create(name=request.POST['name'])
    return redirect('index9')

def create_ninja(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dojo = Dojo.objects.get(id=request.POST['dojo_id'])
        Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
    return redirect('index9')

def delete_dojo(request, dojo_id):
    dojo = Dojo.objects.get(id=dojo_id)
    dojo.delete()
    return redirect('index9')

