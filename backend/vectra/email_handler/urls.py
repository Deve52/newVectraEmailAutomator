from django.urls import path
from . import views

app_name = 'email_handler'

urlpatterns = [
    # Compose URLs
    path("send-bulk-mail/", views.send_bulk_mail, name="send_bulk_mail"),
]
