from django.shortcuts import render, redirect
from .models import Message, Comment
from login_app.models import User

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'messages': Message.objects.all().order_by('-created_at')
    }
    return render(request, 'wall_app/wall.html', context)

def post_message(request):
    user = User.objects.get(id=request.session['user_id'])
    Message.objects.create(user=user, message=request.POST['message'])
    return redirect('/wall')

def post_comment(request, message_id):
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=message_id)
    Comment.objects.create(user=user, message=message, comment=request.POST['comment'])
    return redirect('/wall')

def delete_message(request, message_id):
    message = Message.objects.get(id=message_id)
    if message.user.id == request.session['user_id']:
        message.delete()
    return redirect('/wall')
