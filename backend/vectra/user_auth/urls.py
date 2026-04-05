from django.urls import path
from .views import *

app_name = 'user_auth'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('signup/', signup_user, name="signup"),
]