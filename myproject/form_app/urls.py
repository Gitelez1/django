from django.urls import path
from . import views
                    
urlpatterns = [
    path('app/', views.index3),
    path('users/',views.create_user),
    path('success/', views.success),
]
