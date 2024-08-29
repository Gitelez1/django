from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_course/', views.add_course, name='add_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('course_detail/<int:course_id>/', views.course_detail, name='course_detail'),
    path('delete_course_ajax/<int:course_id>/', views.delete_course_ajax, name='delete_course_ajax'),
]
