import smtplib

from django.contrib.auth import login
from django.shortcuts import render
from .models import Site_Settings
from django.core.mail import send_mail
from django.conf import settings
def emailview(request):
    send=send_mail('hello sepehr','this is new email','sepehrseifpour9877@gmail.com',['sepehrseifpour9877@gmail.com'],fail_silently=False)
    if send:
        print("ok")
    return render(request,"emial.html")
# Create your views here.
