from .bulk_sender import bulk_sender 

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from vectra.org_manager.models import Group
from .models import SentMail

# Compose Mail For Groups
@login_required
def send_bulk_mail(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        body = request.POST.get("body")
        group_ids = request.POST.getlist("group_ids")

        for group_id in group_ids:
            group = Group.objects.filter(id=group_id).first()
            if not group:
                continue

            recipients = list(group.emails.values_list("email", flat=True))

            bulk_sender.send_bulk_emails(request.user, recipients, subject, body)

            SentMail.objects.create(
                group=group,
                subject=subject,
                body=body,
                recipients=", ".join(recipients),
                sender=request.user
            )
        return redirect("core:dashboard_tab", tab="organisation")