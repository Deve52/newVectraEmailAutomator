from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from .core import views

urlpatterns = [
    path("", lambda request: redirect("home/", permanent=False)),
    path("home/", views.home, name="home"),
    path('admin/', admin.site.urls),
]
