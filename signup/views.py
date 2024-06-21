from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm

def signup_action(request):
    global email, password
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse("Failed to save data.")
    else: #method == "GET"
        form = SignupForm()
    return render(request, 'signup/signup.html', {'form':form})

