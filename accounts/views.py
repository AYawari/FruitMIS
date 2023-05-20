from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.
from . import models
from . import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = forms.SiginUpForm(request.POST)
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