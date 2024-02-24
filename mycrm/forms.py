from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    Name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class' : 'from-control'}))
    email=forms.CharField(label='Email Address',widget=forms.TextInput(attrs={'class' : 'from-control'}))
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class' : 'from-control'}))
    password1=forms.CharField(label='Password',widget=forms.TextInput(attrs={'class' : 'from-control'}))
    password2=forms.CharField(label='Password Confirm',widget=forms.TextInput(attrs={'class' : 'from-control'}))
    class Meta:
        model=User
        fields=('Name','email' , 'username' , 'password1', 'password2')
