from django import forms
from . import models

class SiginUpForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = models.User
        fields = ['username', 'email', 'password', 'confirm_password']
