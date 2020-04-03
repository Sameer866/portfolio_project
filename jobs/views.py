from django.shortcuts import render
from django.http import HttpResponse 
from portfolio import settings  
from django.core.mail import send_mail  
  
  
def mail(request):  
    subject = "Greetings"  
    msg     = "Congratulations for your success"  
    to      = "smalik1231990@gmail.com"  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)

# Create your views here.

from .models import job

def home(request):
    jobs=job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})