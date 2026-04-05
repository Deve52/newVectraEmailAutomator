from django.contrib import admin
from django.urls import path, include
from .core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Homepage and Dashboard URLs
    path('', include('vectra.core.urls')),
    # User Authentication And Management URLs
    path('', include('vectra.user_auth.urls')),
    # Organisation Management URLs
    path('', include('vectra.org_manager.urls')),
    # Email Handling URLs
    path('', include('vectra.email_handler.urls')),
]
