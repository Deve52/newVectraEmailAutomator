from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_home, name='forum_home'),
    path('thread/create/', views.create_thread, name='create_thread'),
    path('thread/<int:thread_id>/delete/', views.delete_thread, name='delete_thread'),
    path('thread/<int:thread_id>/modify/', views.modify_thread, name='modify_thread'),
    path('thread/<int:thread_id>/comment/create/', views.create_comment, name='create_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('comment/<int:comment_id>/modify/', views.modify_comment, name='modify_comment'),
]
