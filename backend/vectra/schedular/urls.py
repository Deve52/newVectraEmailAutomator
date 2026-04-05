from django.urls import path
from . import views

app_name = 'schedular'

urlpatterns = [
    path('create/', views.create_schedule, name='create_schedule'),
    path('modify/<int:schedule_id>/', views.modify_schedule, name='modify_schedule'),
    path('delete/<int:schedule_id>/', views.delete_schedule, name='delete_schedule'),
    path('list/<int:user_id>/', views.get_schedules, name='get_schedules'),
]