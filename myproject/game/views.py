import random
from django.shortcuts import render, redirect
from .models import Leaderboard

def start_game(request):
    # Example values, replace these with your actual logic
    max_attempts = 10
    attempts = 3
    remaining_attempts = max_attempts - attempts
    
    context = {
        'max_attempts': max_attempts,
        'attempts': attempts,
        'remaining_attempts': remaining_attempts
    }
    return render(request, 'start_game.html', context)

def guess_number(request):
    if request.method == 'POST':
        try:
            guess = int(request.POST.get('guess', 0))
        except ValueError:
            guess = 0

        number = request.session.get('number')
        attempts = request.session.get('attempts', 0)
        max_attempts = request.session.get('max_attempts', 5)

        if guess < number:
            message = 'Too low!'
        elif guess > number:
            message = 'Too high!'
        else:
            message = f'Congratulations! You guessed the number in {attempts + 1} attempts.'
            request.session['game_status'] = 'won'
            return redirect('submit_name')

        attempts += 1
        request.session['attempts'] = attempts

        if attempts >= max_attempts:
            message = f'You lose! The number was {number}.'
            request.session['game_status'] = 'lost'
            return redirect('submit_name')

        request.session['game_status'] = 'playing'
        return render(request, 'start_game.html', {'message': message})

    return redirect('start_game')

def submit_name(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        attempts = request.session.get('attempts', 0)
        if name and request.session.get('game_status') == 'won':
            Leaderboard.objects.create(name=name, attempts=attempts)
        request.session.flush()
        return redirect('leaderboard')

    return render(request, 'submit_name.html')

def leaderboard(request):
    entries = Leaderboard.objects.all().order_by('attempts')
    return render(request, 'leaderboard.html', {'entries': entries})

