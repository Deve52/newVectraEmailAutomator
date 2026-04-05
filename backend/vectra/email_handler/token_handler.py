# Importing modules
import json, os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
from .models import GmailToken

# Allow HTTP during local development only — never set this in production
if settings.DEBUG:
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

class token_handler:
    # Build an authorization URL to redirect the user to Google
    @staticmethod
    def get_auth_url(redirect_uri):
        flow = Flow.from_client_secrets_file(
            'credential.json',
            scopes=SCOPES,
            redirect_uri=redirect_uri
        )
        auth_url, state = flow.authorization_url(
            access_type='offline',
            prompt='consent'
        )
        return auth_url, state

    # Exchange the OAuth callback code for credentials and save them
    @staticmethod
    def exchange_and_save_token(user, redirect_uri, state, auth_response_url):
        flow = Flow.from_client_secrets_file(
            'credential.json',
            scopes=SCOPES,
            state=state,
            redirect_uri=redirect_uri
        )
        flow.fetch_token(authorization_response=auth_response_url)
        creds = flow.credentials

        GmailToken.objects.update_or_create(
            user=user,
            defaults={
                "token": creds.token,
                "refresh_token": creds.refresh_token or "",
                "client_id": creds.client_id,
                "client_secret": creds.client_secret,
                "expiry": creds.expiry.isoformat() if creds.expiry else ""
            }
        )
    
    @staticmethod
    def fetch_token(user):
        token_obj = user.gmail_token

        return {
            "token": token_obj.token,
            "refresh_token": token_obj.refresh_token,
            "token_uri": "https://oauth2.googleapis.com/token",
            "client_id": token_obj.client_id,
            "client_secret": token_obj.client_secret,
            "scopes": "https://www.googleapis.com/auth/gmail.send",
            "universe_domain": "googleapis.com",
            "account": "",
            "expiry": token_obj.expiry
        }

    @staticmethod
    def has_token(user):
        return GmailToken.objects.filter(user=user).exists()