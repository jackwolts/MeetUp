from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
            print("user created")
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('login')

    return render(request, "register.html")


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,"invailed credentials")
            return redirect('login')
    return render(request,"login.html")



def index(request):
    return render(request,"index.html",{'name':request.user.username})

def videocall(request):
    return render(request,"videocall.html",{'name':request.user.username})

def join(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/videocall?roomID=" + roomID)
    return render(request,"join.html")