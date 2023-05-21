from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from . import models
from . import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# def register(request):
#     if request.method == 'POST':
#         form = forms.SiginUpForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             return HttpResponse('the data is not valid  try again')    
#     else:
#         form = forms.SiginUpForm()
#         return render(request, 'accounts/singnup.html', {'form':form}



def register(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        # Check if passwords match
        if password != re_password:
            raise ValidationError("Passwords do not match")

        # Check if username is already taken
        if models.User.objects.filter(username=username).exists():
            raise ValidationError("Username already taken")

        # Check if email is already taken
        if models.User.objects.filter(email=email).exists():
            raise ValidationError("Email already taken")

        # # Other restrictions
        # if len(password) < 4:
        #     raise ValidationError("Password must be at least 8 characters long")
        # if not any(char.isdigit() for char in password):
        #     raise ValidationError("Password must contain at least one digit")
        # if not any(char.isalpha() for char in password):
        #     raise ValidationError("Password must contain at least one letter")

        # Create user
        user = models.User.objects.create_user(username, email, password)
        user.save()
        return redirect('home')
    

        # Authenticate user and login
        # user = authenticate(request,username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('home')

    return render(request, 'accounts/singnup.html')


def login_page(request):
    if request.method == 'POST':
        email = request.POST['email'] 
        password = request.POST['password']
       
        try:
            user = models.User.objects.get(email=email) 
            
        except:
            messages.error(request, 'user does not exist!!!')
        user = authenticate(request, email=email, password=password)
       
        if user is not None:
            login(request,user)
            
            return redirect('home')
        else:
            messages.error(request, 'incorrect email or password')

              
    return render(request , 'accounts/login.html')    
                 
