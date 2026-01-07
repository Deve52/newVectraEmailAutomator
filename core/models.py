from django.db import models
from django.contrib.auth.models import User


class Organisation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name


class Group(models.Model):
    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        related_name='groups',
        null=True
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('organisation', 'name')

    def __str__(self):
        return self.name


class GroupEmail(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='emails'
    )
    email = models.EmailField()

    class Meta:
        unique_together = ('group', 'email')

    def __str__(self):
        return self.email

class SentMail(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
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

class Schedule(models.Model):
    SCHEDULE_TYPES = [
        ('once', 'Run Once'),
        ('daily', 'Every Day'),
        ('weekly', 'Specific Days of Week'),
        ('monthly_nth', 'Every Nth Day of Month'),
        ('yearly_nth', 'Nth Day of Month Once in Year'),
    ]

    name = models.CharField(max_length=255, default="Unnamed Schedule")
    description = models.TextField(null=True, blank=True)

    schedule_type = models.CharField(max_length=20, choices=SCHEDULE_TYPES)

    # For "once"
    run_datetime = models.DateTimeField(null=True, blank=True)

    # For "daily"
    run_time = models.TimeField(null=True, blank=True)

    # For "weekly"
    # Store list of weekdays as integers (0=Monday ... 6=Sunday)
    weekdays = models.JSONField(null=True, blank=True)

    # For monthly patterns (1–31)
    nth_day = models.PositiveIntegerField(null=True, blank=True)

    # For yearly patterns (1-12)
    month = models.PositiveIntegerField(null=True, blank=True)

    # Generic metadata
    last_run = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.schedule_type)