from django import forms
from . import models

class SiginUpForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = models.User
        fields = ['username', 'email', 'password', 'confirm_password']
    
    def clean_password_confirm(self):
        password = self.cleaned_data.get['password']
        confirm_password = self.cleaned_data.get('confirm_password')

       
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("The two password fields must match.")
        return confirm_password