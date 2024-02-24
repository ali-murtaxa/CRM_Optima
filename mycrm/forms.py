from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    Name=forms.CharField(label='Name',widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    email=forms.CharField(label='Email Address',widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    username=forms.CharField(label='Username',widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2=forms.CharField(label='Password Confirm',widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        model=User
        fields=('Name','email' , 'username' , 'password1', 'password2')
