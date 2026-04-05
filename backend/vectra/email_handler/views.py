from .bulk_sender import bulk_sender
from .token_handler import token_handler

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from vectra.org_manager.models import Group
from .models import SentMail

OAUTH_REDIRECT_URI_NAME = "email_handler:gmail_oauth_callback"


def _build_redirect_uri(request: HttpRequest) -> str:
    from django.urls import reverse
    return request.build_absolute_uri(reverse(OAUTH_REDIRECT_URI_NAME))


# Compose Mail For Groups
@login_required
def send_bulk_mail(request):
    # If no Gmail token yet, kick off the OAuth flow
    if not token_handler.has_token(request.user):
        redirect_uri = _build_redirect_uri(request)
        auth_url, state = token_handler.get_auth_url(redirect_uri)

        # Stash the state + where to go after auth so the callback can resume
        request.session["gmail_oauth_state"] = state
        request.session["gmail_oauth_next"] = request.get_full_path()

        return redirect(auth_url)

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


# Gmail OAuth callback — Google redirects the user's browser here after granting access
@login_required
def gmail_oauth_callback(request):
    state = request.session.get("gmail_oauth_state")
    next_url = request.session.pop("gmail_oauth_next", None)

    redirect_uri = _build_redirect_uri(request)

    token_handler.exchange_and_save_token(
        user=request.user,
        redirect_uri=redirect_uri,
        state=state,
        auth_response_url=request.build_absolute_uri()
    )

    # Return the user to where they were originally headed, or fall back to dashboard
    if next_url:
        return redirect(next_url)
    from django.urls import reverse
    return redirect(reverse("core:dashboard_tab", kwargs={"tab": "organisation"}))