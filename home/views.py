
from datetime import date, timedelta
import datetime
import logging

from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin, logout
from home.models import Reviews,Bookingreq,Room

# Create your views here.


def index(request):
    if request.method=='POST':
        if(request.user.is_authenticated):
            msg = request.POST.get('message')
            uname = request.user.username
            print(msg,uname)
            rev = Reviews(name=uname,txt=msg)
            rev.save()
    
    current_date = date.today().strftime('%Y-%m-%d')
    cd = date.today() + timedelta(days=1)
    current_date2 = cd.strftime('%Y-%m-%d')

    datedata={
        'current_date':current_date,
        'current_date2':current_date2
    }

    return render(request,'index.html', datedata)


def mybookings(request):
    
    if(not request.user.is_authenticated):
        return redirect('login')
    
    displaydata = Bookingreq.objects.filter(name=request.user.username)
 
    data={
        'servicedata':displaydata
    }
    
    return render(request,'mybookings.html',data)    

def rooms(request):
    if(not request.user.is_authenticated):
        return redirect('login')
    indate = request.GET.get("chkin","")
    outdate = request.GET.get("chkout","")
    num = request.GET.get("purp","")
    if(num==1):
        purp='guest'
    
    elif(num==2):
        purp='placement'
    
    else:
        purp='fest'
    uname = request.user.username

    displaydata = Room.objects.all()
 
    data={
        'servicedata':displaydata
    }

    if request.method=='POST':
        rt = request.POST.get('form_id')
        count = request.POST.get('roomcount')
        if(rt=='luxury'):
            cost=1000*int(count)
        else:
            cost=500*int(count)
        print(cost)    
        dbobj = Bookingreq(name=uname,chckindate=indate,chckoutdate=outdate,purpose=purp,roomtype=rt,noofrooms=count,tcost=cost,rstatus='pending')
        dbobj.save()
        return redirect('mybookings')
    return render(request,'roomtobook.html',data)
 


def signup(request):
    if request.method=='POST':
        email = request.POST.get('email')
        uname = request.POST.get('username')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        otp = request.POST.get('otp')
        print(otp)
        if User.objects.filter(username=uname).exists():
            messages.error(request, "username already exists")
        if(len(pass1)<5):
            messages.error(request, "password should be more than 5 characters")
        #username
        elif pass1!=pass2:
            messages.error(request, "passwords dont match")
        else:
                myuser = User.objects.create_user(uname,email,pass1)
                myuser.save()
                return redirect('login')
        print(email,uname,pass1,pass2)
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request, username=uname, password=passw)
        # if not user.is_email_verified:
    
        if user is not None:
            authlogin(request, user)
            return redirect('home')
        else:
            messages.error(request, "credentials do not match")
    return render(request,'login.html')


def logoutuser(request):
    logout(request)
    return redirect('home')