from django.contrib import admin
from django.urls import path, include
from tvshows import views
from . import views

urlpatterns = [
    path('shows/<int:id>/update/', views.update_show, name='update_show'),
    path('admin/', admin.site.urls),
    path('', views.root, name='root'),  # This is the line causing the issue
    path('', include('tvshows.urls')),
]
