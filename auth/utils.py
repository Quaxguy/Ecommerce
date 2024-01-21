import random
# from twilio.rest import Client
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from auth.models import OneTimeToken,User
import uuid


def generateEmailToken():
   email_token=str(uuid.uuid4())
   return email_token


def send_email_verification_mail(email,request):
   
    subject = "Verify your email address"
    token=generateEmailToken()
    verification_link = f"http://127.0.0.1:8000/api/v1/auth/verify-email/{token}/" #front end domain
    user=User.objects.get(email=email)
    # Compose and send the verification email
    message = f"Hi {user.first_name},\n\nPlease click on the following link to verify your email address:\n\n{verification_link}"
    from_email = settings.EMAIL_HOST_USER
    to_email = user.email
    OneTimeToken.objects.create(user=user,email_token=token)
   # send_mail(subject, message, from_email,[to_email],fail_silently=False)
    email=EmailMessage(subject,message,from_email,to=[to_email])
    email.send()

def send_normal_email(data):
    email=EmailMessage(
        subject=data['email_subject'],
        body=data['email_body'],
        from_email=settings.EMAIL_HOST_USER,
        to=[data['to_email']]
    )
    email.send()  
