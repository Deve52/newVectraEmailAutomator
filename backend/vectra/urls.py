from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from .core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # User Authentication And Management URLs
    path('', include('vectra.user_auth.urls')),
    
    # Home Page
    path("", lambda request: redirect("home/", permanent=False)),
    path("home/", views.home, name="home"),
    
    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
    
    
]
