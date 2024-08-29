"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogs.urls')),  # Direct all root URLs to the blogs app
    path('app-name/', include('app_name.urls')),
    path('time/', include('time_display.urls')),
    path('form/', include('form_app.urls')),
    path('dojo/', include('dojo_survey.urls')),
    path('main1/', include('main.urls')),
    path('game1/', include('game.urls')),
    path('ninja-gold/', include('ninja.urls')),
    path('surveys/', include('surveys.urls')),
    path('users/', include('users.urls')),
    path('movie/', include('movie.urls')),
    path('ninja/', include('dojo_ninjas_app.urls')),
    path('liber/', include('books_authors_app.urls')),
]
