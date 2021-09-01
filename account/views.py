from django.shortcuts import render, redirect
from django.contrib import  messages
from . models import *
from django.contrib.auth.models import auth
# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid details')
            return redirect('log')
    else:

        return render(request,'login.html')
def regi(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if ash.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('reg')
            elif ash.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('reg')
            else:
                use=ash.objects.create(username=username,firstname=firstname,email=email,password1=password1)
                use.save()
            return redirect('home')
        else:
            messages.info(request,'password does not mach ')
            return redirect('reg')

    else:

        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')