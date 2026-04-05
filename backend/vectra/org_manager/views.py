from django.shortcuts import render

import csv, io
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Organisation, Group, GroupEmail

# Create Organisation Popup From
@login_required
def create_organisation(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        csv_file = request.FILES.get("csv_file")

        # Creating Organisation
        organisation = Organisation.objects.create(
            user=request.user,
            name=name,
            description=description
        )

        # If User provided CSV then add groups
        if csv_file:
            decoded = csv_file.read().decode("utf-8")
            reader = csv.reader(io.StringIO(decoded))

            # Skipping the first row because it contains column names
            next(reader, None)
            for row in reader:
                if len(row) < 2:
                    continue
                group_name = row[0].strip()
                email = row[1].strip()

                if not group_name or not email:
                    continue
                # Creating Group with emails
                group_obj, _ = Group.objects.get_or_create(organisation=organisation, name=group_name)
                GroupEmail.objects.get_or_create(group=group_obj,email=email)

        return redirect("core:dashboard_tab", tab="organisation")
        # I might write comments to explain the code in the future

# Modify Existing Organisation
@login_required
def modify_organisation(request):
    if request.method == "POST":
        org_id = request.POST.get("org_id")   # You need to send this hidden input
        org = get_object_or_404(Organisation, id=org_id)

        org.name = request.POST.get("name", "").strip()
        org.description = request.POST.get("description", "").strip()
        org.save()

    url = reverse("core:dashboard_tab", kwargs={"tab": "organisation"})
    url = f"{url}?popup=editOrganisationPopup&id={org_id}"
    return redirect(url)

# Delete an Organisation
@login_required
def delete_organisation(request):
    organisation = get_object_or_404(
        Organisation,
        id=request.POST.get("organisation_id"),
        user=request.user
    )

    if request.method == "POST":
        organisation.delete()
        return redirect("core:dashboard_tab", tab="organisation")

    return redirect("core:dashboard_tab", tab="organisation")

# Group Popup forms
@login_required
def create_group(request):
    if request.method == "POST":
        name = request.POST.get("name")
        recipients_raw = request.POST.get("recipients")
        org_id = request.POST.get("org_id")

        try:
            organisation = Organisation.objects.get(id=org_id, user=request.user)
        except Organisation.DoesNotExist:
            messages.error(request, "Invalid organisation.")
            return redirect("core:dashboard")

        if Group.objects.filter(organisation=organisation, name=name).exists():
            messages.error(request, "A group with that name already exists.")
            return redirect("core:dashboard")

        group = Group.objects.create(
            organisation=organisation,
            name=name,
            description=None
        )
        if recipients_raw:
            emails = [e.strip() for e in recipients_raw.split(",") if e.strip()]

            for email in emails:
                if "@" in email:
                    parts = email.split("@")
                    if len(parts) == 2:
                        local, domain = parts
                        if local and domain and "." in domain and " " not in email:
                            GroupEmail.objects.create(group=group, email=email)

        url = reverse("core:dashboard_tab", kwargs={"tab": "organisation"})
        url = f"{url}?popup=editOrganisationPopup&id={org_id}"
        return redirect(url)

# Modify Group
@login_required
def modify_group(request):
    if request.method == "POST":
        org_id = request.POST.get("org_id")
        group_id = request.POST.get("group_id")
        name = request.POST.get("name")
        recipients_raw = request.POST.get("recipients", "")

        try:
            group = Group.objects.get(id=group_id, organisation__user=request.user)
        except Group.DoesNotExist:
            return redirect("core:dashboard")

        group.name = name
        group.save()

        emails = [
            email.strip()
            for email in recipients_raw.split(",")
            if email.strip() != ""
        ]

        GroupEmail.objects.filter(group=group).delete()
        group_emails = [
            GroupEmail(email=email, group=group)
            for email in emails
        ]
        GroupEmail.objects.bulk_create(group_emails)

    url = reverse("core:dashboard_tab", kwargs={"tab": "organisation"})
    url = f"{url}?popup=editOrganisationPopup&id={org_id}"
    return redirect(url)

# Delete Group
@login_required
def delete_group(request):
    org_id = request.POST.get("org_id")
    group_id = request.POST.get("group_id")
    group = Group.objects.filter(id=group_id, organisation__user=request.user).first()

    if not group:
        messages.error(request, "Group not found.")
        return redirect("core:dashboard")

    group.delete()
    url = reverse("core:dashboard_tab", kwargs={"tab": "organisation"})
    url = f"{url}?popup=editOrganisationPopup&id={org_id}"
    return redirect(url)