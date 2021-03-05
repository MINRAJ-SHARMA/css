from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        return render(request,'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get['username']
        password = request.POST.get['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    else:
        return render(request,'login.html')




def logoutUser(request):
    logout(request)
    return render(request,'/login')
