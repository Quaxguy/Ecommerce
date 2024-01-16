import random
# from twilio.rest import Client
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

def send_email_verification_mail(user,token):
   
    verification_link = f"http://127.0.0.1:8000/api/verify-email/{token}/" #front end domain
    # Compose and send the verification email
    subject = "Verify your email address"
    message = f"Hi {user.email},\n\nPlease click on the following link to verify your email address:\n\n{verification_link}"
    from_email = settings.EMAIL_HOST_USER
    to_email = user.email
   # send_mail(subject, message, from_email,[to_email],fail_silently=False)
    email=EmailMessage(subject,message,from_email,to=[to_email])
    email.send()


            
