from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SentMail(models.Model):
    group = models.ForeignKey("org_manager.Group", on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    recipients = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} ({self.group.name})"

class GmailToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="gmail_token")
    token = models.TextField()
    refresh_token = models.TextField()
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
    expiry = models.CharField(max_length=255)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Gmail Token for {self.user.username}"