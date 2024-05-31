from typing import Any
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username')
    email = forms.CharField(max_length=30, label='Email')
    password = forms.CharField(min_length=4, label='Password', widget=forms.PasswordInput)
    confirm = forms.CharField(min_length=4, label='Password confirm', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        confirm = self.cleaned_data['confirm']

        if password and confirm and password != confirm:
            raise forms.ValidationError('Passwords are not same')
        
        if not '@' in email:
            raise forms.ValidationError('Please write correct email address')
        
        values = {
            "username": username,
            "email": email,
            "password": password,
            "confirm": confirm
        }

        return values
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username')
    email = forms.CharField(max_length=30, label='Email')
    password = forms.CharField(min_length=4, label='Password', widget=forms.PasswordInput)