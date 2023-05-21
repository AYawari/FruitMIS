from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from . import models
from . import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = forms.SiginUpForm(request.POST)
        # password = form.cleaned_data.get('password')
        # print(password)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('the data is not valid  try again')    
    else:
        form = forms.SiginUpForm()
        return render(request, 'accounts/singnup.html', {'form':form})


def home(request):
    return HttpResponse('home page')   

def login(request):
    if request.method == 'POST':
        email = request.POST['email'] 
        password = request.POST['password']
        print(email)
        try:
            user = models.User.objects.get(email=email) 
            print(user)
        except:
            messages.error(request, 'user does not exist!!!')
        user = authenticate(request, email=email, password=password)
        print(user)
        if user:
            user.save()
            print(user)
            messages.success(request, 'successfully login')
            return redirect('home')
        else:
            messages.error(request, 'incorrect email or password')

              
    return render(request , 'accounts/login.html')    
                

