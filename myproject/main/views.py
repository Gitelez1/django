from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def root_view(request):
    # Initialize counter if not already set
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if 'visit_count' not in request.session:
        request.session['visit_count'] = 0

    # Increment visit count
    request.session['visit_count'] += 1

    # Get current counter value
    counter = request.session['counter']
    visit_count = request.session['visit_count']

    # Render template with counter and visit count
    return render(request, 'index5.html', {'counter': counter, 'visit_count': visit_count})

def destroy_session(request):
    # Clear session data
    request.session.flush()
    return redirect('/main1/one/')
    
def increment_counter(request, amount=2):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += int(amount)
    return redirect('/main1/one/')