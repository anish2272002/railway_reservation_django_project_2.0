from django.shortcuts import render

from django.template.loader import get_template
from django.core.mail import EmailMessage  
from django.conf import settings

from .models import user
# Create your views here.

def login(request):
    for usr in user.objects.all().filter(verified=False):
        usr.delete()
    return render(request,'index.html')

def sign(request):
    for usr in user.objects.all().filter(verified=False):
        usr.delete()
    return render(request,'sign.html')

def confirmation(request):
    usr=user()
    usr.email=request.POST['email']
    usr.password=request.POST['password']
    usr.fname=request.POST['fname']
    usr.lname=request.POST['lname']
    usr.dob=request.POST['dob']
    usr.gender=request.POST['gender']
    for u in user.objects.all():
        if usr.email==getattr(u,'email'):
            return render(request,"acc_already_exist.html",{'email':usr.email})
    else:
        usr.save()
        email_link_path='claim-account-confirmation-token-ff9dcccf380287f026b3ecc819643'
        message=get_template('email.html').render({'fname':usr.fname,'lname':usr.lname,'email':usr.email,'email_link':'http://172.25.160.1:7000/'+email_link_path})
        msg=EmailMessage('Rail Co.',message,settings.EMAIL_HOST_USER,[usr.email])
        msg.content_subtype = 'html'
        msg.send()
        return render(request,"confirmation.html",{'email':usr.email})
        

def confirmed(request):
    usr=user.objects.last()
    usr.verified = True
    usr.save()
    return render(request,"confirmed.html")

def dash(request):
    test_email=request.POST["email"]
    test_password=request.POST["password"]
    for u in user.objects.all():
        if test_email==getattr(u,'email'):
            if test_password==getattr(u,'password'):
                return render(request,'dash.html',{'email':test_email,'password':test_password})
            else:
                return render(request,"incorrect_password.html")
    else:
        return render(request,"acc_not_exist.html")