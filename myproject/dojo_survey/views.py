# from django.shortcuts import render, redirect

# # Create your views here.

# def index4(request):
#     return render(request, 'index4.html')

# def form_post(request):
#     if request.method == 'POST':
#         # Print POST data for debugging
#         print(request.POST)
        
#         context = {
#             'name': request.POST.get('name'),
#             'dojo_location': request.POST.get('dojo_location'),
#             'favorite_language': request.POST.get('favorite_language'),
#             'comment': request.POST.get('comment')
#         }
#         return redirect('/result')
#     return redirect('/')

# def result(request):
#     # You would typically use session or another method to pass data
#     return render(request, 'result.html')


# def form_post(request):
#     if request.method == 'POST':
#         # Process the form data
#         return redirect('/dojo/result/')
#     return render(request, "index4.html")

# def result(request):
#     # Extract data from session or context
#     context = {
#         'name_on_template': request.session.get('name'),
#         'email_on_template': request.session.get('email'),
#         'favorite_language': request.session.get('favorite_language'),
#         'comment': request.session.get('comment')
#     }
#     return render(request, 'result.html', context)

# def form_post(request):
#     if request.method == 'POST':
#         request.session['name'] = request.POST.get('name')
#         request.session['email'] = request.POST.get('email')
#         return redirect('/dojo/result/')
#     return render(request, "index4.html")

from django.shortcuts import render, redirect

def index4(request):
    return render(request, "index4.html")

def form_post(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dojo_location = request.POST.get('dojo_location')
        favorite_language = request.POST.get('favorite_language', 'None')
        comment = request.POST.get('comment', 'None')
        
        # Save data in session or pass directly to context for the redirect
        request.session['name'] = name
        request.session['dojo_location'] = dojo_location
        request.session['favorite_language'] = favorite_language
        request.session['comment'] = comment
        
        return redirect('/dojo/result/')
    return redirect('/dojo/survey/')

def result(request):
    context = {
        'name_on_template': request.session.get('name', 'None'),
        'dojo_location_on_template': request.session.get('dojo_location', 'None'),
        'favorite_language_on_template': request.session.get('favorite_language', 'None'),
        'comment_on_template': request.session.get('comment', 'None'),
    }
    return render(request, 'result.html', context)
