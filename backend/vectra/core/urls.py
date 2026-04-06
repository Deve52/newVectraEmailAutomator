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

    # Test Pages3
    path("test/", views.test_page, name="test_page"),
    path("forum-test/", views.forum_test_page, name="forum_test_page"),
]
