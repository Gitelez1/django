from django.shortcuts import render, redirect
from time import gmtime, strftime

def index1(request):
    context = {
        'time': strftime("%Y-%m-%d %H:%M:%S", gmtime())
    }
    return render(request, 'index1.html', context)


def index2(request):
    if request.method == "GET":
        print("a GET request is being made to this route")
        return render(request, "index2.html")
    if request.method == "POST":
        print("a POST request is being made to this route")
        return redirect("/")


from django.shortcuts import render, redirect
def index3(request):
    if request.method == "GET":
        print(request.GET)
    if request.method == "POST":
        print(request.POST)


def index4(request):
    if request.method == "POST":
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]
