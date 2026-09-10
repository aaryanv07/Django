from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
# Create your views here.
def register_view(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            messages.success(request,f'Account created successfully for {user}')
            return redirect('dashboard')
        else:
            messages.error(request,'Failed to create account')
    else:
        form=RegistrationForm()
    return render(request,'acounts/register.html',{'form':form})


def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f'Logged in successfully as {user}')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
    return render(request,'acounts/login.html')


@login_required(login_url='login')
def dashboard_view(request):
    return render(request,'acounts/dashboard.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('login')
