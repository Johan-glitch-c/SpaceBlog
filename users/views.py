from django.conf.global_settings import LOGIN_URL
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect

import users
from .forms import User_Form, LoginForm
from .models import User
from django.contrib import auth
# Create your views here.
def register(request):

    if request.method == 'POST':
        form = User_Form(data=request.POST)
        if form.is_valid():
            if not User.objects.filter(username=form.cleaned_data['username']).exists():
                User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'])

                return redirect('users:login')

    else:
        form = User_Form()
    context = {'form':form}
    return render(request,'register.html',context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                return redirect('index')

    else:
        form = LoginForm()
    context = {'form':form}
    return render(request,'login.html',context)