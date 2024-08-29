from django.shortcuts import render, redirect
import random

# Create your views here.
def index6(request):
    # Your code to render the index page
    return render(request, 'index6.html')  # Adjust template name as needed


def process_money(request, location):
    # Initialize session variables if they don't exist
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'moves' not in request.session:
        request.session['moves'] = 0
    if 'goal' not in request.session:
        request.session['goal'] = 100  # Set a default goal, or handle this differently

    # Process the location and update the session
    gold_earned = 0
    message = ""

    if location == 'farm':
        gold_earned = random.randint(10, 20)
        message = f"Earned {gold_earned} gold from the farm!"
    elif location == 'cave':
        gold_earned = random.randint(5, 10)
        message = f"Earned {gold_earned} gold from the cave!"
    elif location == 'house':
        gold_earned = random.randint(2, 5)
        message = f"Earned {gold_earned} gold from the house!"
    elif location == 'casino':
        gold_earned = random.randint(-50, 50)
        if gold_earned >= 0:
            message = f"Earned {gold_earned} gold from the casino!"
        else:
            message = f"Lost {-gold_earned} gold at the casino!"
    else:
        # Handle unknown location
        return redirect('index6')

    # Update session data
    request.session['gold'] += gold_earned
    request.session['activities'].append(message)
    request.session['moves'] += 1

    if request.session['gold'] >= request.session['goal']:
        request.session['activities'].append('Congratulations! You reached your goal!')
        request.session['gold'] = 0  # Reset or handle as needed

    return redirect('index6')