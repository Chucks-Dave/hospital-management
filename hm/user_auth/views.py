from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib import auth

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_super_user:
            if user.is_active:
                auth.login(request, user)
                return redirect('home')
        elif user is not None and user.staff_type == 'doctor':
            if user.is_active:
                auth.login(request, user)
                return redirect('doctor_dashboard', username)
        elif user is not None and user.staff_type == 'none':
            if user.is_active:
                auth.login(request, user)
                return redirect('patient_dashboard', username)
        else:
            return redirect('login')
    context = {}
    return render(request, "user_auth/login.html", context)


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff_type = 'none'
            instance.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, "user_auth/register.html", context)


def logout(request):
    auth.logout(request)
    return redirect('home')
