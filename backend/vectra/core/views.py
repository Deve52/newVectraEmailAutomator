import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from vectra.org_manager.models import Organisation, Group
from vectra.email_handler.models import SentMail


def home(request):
    return render(request, "home.html")

@login_required
def dashboard(request, tab="home"):
    popup = request.GET.get("popup")
    popup_id = request.GET.get("id")
    
    avatar = request.user.first_name[0].upper() + request.user.last_name[0].upper()
    full_name = request.user.first_name + " " + request.user.last_name

    organisations = Organisation.objects.filter(user=request.user)

    groups = Group.objects.filter(
        organisation__user=request.user
    ).prefetch_related('emails')

    history = SentMail.objects.filter(
        sender=request.user
    ).select_related('group').order_by('-created_at')


    org_groups = {}

    for org in organisations:
        groups_list = []
        for g in org.groups.all():
            emails = g.emails.values_list("email", flat=True)
            recipients = ",".join(emails)

            groups_list.append({
                "id": g.id,
                "name": g.name,
                "recipients": recipients
            })
        org_groups[org.id] = groups_list

    org_details = {
        org.id: { "name": org.name, "description": org.description or ""}
        for org in organisations
    }

    return render(request, "dashboard.html", {
        "current_tab": tab,
        "current_popup": popup,
        "popup_id": popup_id,
        "full_name": full_name,
        "avatar": avatar,
        "organisations": organisations,
        "groups": groups,
        "history": history,
        "org_groups": json.dumps(org_groups, cls=DjangoJSONEncoder),
        "org_details": json.dumps(org_details, cls=DjangoJSONEncoder)
    })