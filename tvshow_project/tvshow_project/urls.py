"""
URL configuration for tvshow_project project.

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
from django.urls import path
from tvshows import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.root, name='root'),
    path('shows/', views.all_shows, name='all_shows'),
    path('new/', views.new_show, name='new_show'),
    path('create/', views.create_show, name='create_show'),
    path('<int:id>/', views.show_detail, name='show_detail'),
    path('<int:id>/edit/', views.edit_show, name='edit_show'),
    path('<int:id>/update/', views.update_show, name='update_show'),
    path('<int:id>/destroy/', views.destroy_show, name='destroy_show'),
    path('check_title/', views.check_title, name='check_title'),
]