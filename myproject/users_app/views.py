from django.shortcuts import render
from django.http import HttpResponse

# other imports
from .models import Movie
# show all of the data from a table
def index7(request):
    context = {
        "all_the_movies": Movie.objects.all()
    }
    return render(request, "index7.html", context)


def first_view(request):
    # Example list of users
    users = [{'id': 1, 'username': 'john_doe'}, {'id': 2, 'username': 'jane_smith'}]  # Replace with actual user data
    return render(request, 'index8.html', {'users': users})

def second_view(request):
    return HttpResponse("HELLO YOU")