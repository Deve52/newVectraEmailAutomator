from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = 'core'

urlpatterns = [
    # Home Page
    path("", lambda request: redirect("home/", permanent=False)),
    path("home/", views.home, name="home"),
    
    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/<str:tab>/", views.dashboard, name="dashboard_tab"),
]