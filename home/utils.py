from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

def send_email_client():
    subject = ""
    message = ""
    from_email = settings.EMAIL_HOST_USER
    
    send_mail()
