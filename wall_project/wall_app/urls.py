from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall),
    path('post_message', views.post_message),
    path('post_comment/<int:message_id>', views.post_comment),
    path('delete_message/<int:message_id>', views.delete_message),
]
