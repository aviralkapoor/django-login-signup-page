from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse
from .forms import LoginForm

def welcome(request):
    return render(request, 'login/welcome.html')

def error(request):
    return render(request, 'login/error.html')

def login_action(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            #form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('welcome')
            else:
                return redirect('error')
        else:
            return HttpResponse("Failed to save data.")
    else: #method == "GET"
        form = LoginForm()
    return render(request, 'login/login.html', {'form':form})

def logout_action(request):
    logout(request)
    return redirect('login')