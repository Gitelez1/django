from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoize",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)

def some_function(request):
    request.session['name'] = request.POST['name']
    request.session['counter'] = 100

