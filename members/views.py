from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import UserRegisterForm
from django import forms


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully")
            return redirect('home')
        
        else:
            messages.success(request, "There was an Error in Logging in, Try Again!!!")
            return redirect('login')
        
    else:
        return render(request, "authenticate/login.html", {})
    
    
    
def logout_user(request):
    logout(request)
    messages.success(request, "You were Logged Out")
    return redirect('home')



def register_user(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered, Kindly Log in')
            return redirect('login')
       
    
    return render(request, "authenticate/register.html", {'form':form})
    
    

    
   
        
        
        
    
    

    
    
    


       

    
        
    
    
    
    
    
    
    
    


