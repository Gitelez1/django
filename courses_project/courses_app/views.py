from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Course, Description, Comment
from django.http import JsonResponse

def index(request):
    courses = Course.objects.all()
    return render(request, 'courses_app/index.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        name = request.POST['name']
        description_text = request.POST['description']

        try:
            description = Description.objects.create(content=description_text)
            Course.objects.create(name=name, description=description)
        except ValidationError as e:
            return render(request, 'courses_app/index.html', {'errors': e, 'courses': Course.objects.all()})

    return redirect('/')

def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('/')
    return render(request, 'courses_app/delete.html', {'course': course})

from .models import Course, Description, Comment

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        comment_content = request.POST['comment']
        Comment.objects.create(content=comment_content, course=course)
    return render(request, 'courses_app/course_detail.html', {'course': course})

def delete_course_ajax(request, course_id):
    if request.method == 'POST':
        course = Course.objects.get(id=course_id)
        course.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})
