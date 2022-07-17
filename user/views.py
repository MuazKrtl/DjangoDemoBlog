from wsgiref.util import request_uri
from django.shortcuts import render,redirect

import user
from .forms import LoginForm, RegisterForm

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

# Create your views here.
def register(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
                
        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.info(request,"Kayıt Başarılı!")
        return redirect("index")

    context = {
        "form":form
    }
    return render(request,"register.html",context)




        
    """if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            newUser = User(username=username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser)
            return redirect("index")
        
    
        context = {
            "form":form
        }
        return render(request,"register.html",context)    

    else:
        form = RegisterForm()
        context = {
            "form":form
        }
        return render(request,"register.html",context)"""



    """form = RegisterForm()
    context = {
        "form":form
    }
    return render(request,"register.html",context)"""

def user_login(request):
    form = LoginForm(request.POST or None)
    
    context = {
            "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)
        if user is None :
            messages.info(request,"Kullanıcı adı veya Parola yanlış!")
            return render(request,"login.html",context)
        
        messages.success(request,"Başarıyla Giriş Yapıldı")
        login(request,user)
        return redirect("index")

    return render(request,"login.html",context)

def user_logout(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yapıldı")
    return redirect("index")
