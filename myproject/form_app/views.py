from django.shortcuts import render, redirect

# Create your views here.

def index3(request):
    return render(request,"index3.html")


# def create_user(request):
#     print("Got Post Info....................")
#     print(request.POST)
#     return render(request,"index3.html")


# def create_user(request):
#     print("Got Post Info....................")
#     name_from_form = request.POST['name']
#     email_from_form = request.POST['email']
#     print(name_from_form)
#     print(email_from_form)
#     return render(request,"index3.html")


def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context = {
        "name_on_template" : name_from_form,
        "email_on_template" : email_from_form
    }
    return redirect("/form/success")


def success(request):
    # this is the success route
    return render(request, "success.html")