from django.urls import path
from . import views

app_name = 'email_handler'

urlpatterns = [
    # Compose URLs
    path("send-bulk-mail/", views.send_bulk_mail, name="send_bulk_mail"),
    path("gmail/callback/", views.gmail_oauth_callback, name="gmail_oauth_callback"),
    path("templates/create/", views.create_email_template, name="create_email_template"),
]