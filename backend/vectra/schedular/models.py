from django.db import models
from django.contrib.auth.models import User
from vectra.email_handler.models import EmailTemplate
from vectra.org_manager.models import Group

class EmailSchedule(models.Model):
    SCHEDULE_TYPE_CHOICES = [
        ('once', 'Run Once'),
        ('daily', 'Run Everyday'),
        ('weekly', 'Specific Days of Week'),
        ('monthly', 'Every Nth Day of Month'),
        ('yearly', 'Nth Day Once a Year'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    schedule_type = models.CharField(max_length=10, choices=SCHEDULE_TYPE_CHOICES)
    
    # For 'once'
    run_once_datetime = models.DateTimeField(null=True, blank=True)
    
    # For 'daily', 'weekly', 'monthly', 'yearly'
    time = models.TimeField(null=True, blank=True)
    
    # For 'weekly'
    days_of_week = models.CharField(max_length=15, blank=True, null=True, help_text="Comma-separated day numbers (0=Sun, 1=Mon, ...)")
    
    # For 'monthly'
    day_of_month = models.IntegerField(null=True, blank=True, help_text="Day of the month (1-31)")
    
    # For 'yearly'
    yearly_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    last_run_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.template.name} for {self.group.name} - {self.get_schedule_type_display()}"