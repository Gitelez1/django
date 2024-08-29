from django.shortcuts import render, redirect, get_object_or_404
from .models import Show
from .forms import ShowForm
from django.http import JsonResponse


def root(request):
    return redirect('/shows')

def new_show(request):
    form = ShowForm()
    return render(request, 'new.html', {'form': form})

def create_show(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/shows/{form.instance.id}')
        else:
            return render(request, 'new.html', {'form': form})

def show_detail(request, id):
    show = get_object_or_404(Show, id=id)
    return render(request, 'detail.html', {'show': show})

def all_shows(request):
    shows = Show.objects.all()
    return render(request, 'all_shows.html', {'shows': shows})

def edit_show(request, id):
    show = get_object_or_404(Show, id=id)
    form = ShowForm(instance=show)
    return render(request, 'edit.html', {'form': form, 'show': show})

def update_show(request, id):
    show = get_object_or_404(Show, id=id)
    if request.method == 'POST':
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            form.save()
            return redirect(f'/shows/{show.id}')
        else:
            return render(request, 'edit.html', {'form': form, 'show': show})

def destroy_show(request, id):
    show = get_object_or_404(Show, id=id)
    show.delete()
    return redirect('all_shows')


def check_title(request):
    title = request.GET.get('title', None)
    data = {
        'is_taken': Show.objects.filter(title__iexact=title).exists()
    }
    return JsonResponse(data)