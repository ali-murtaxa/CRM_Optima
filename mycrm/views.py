from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST['']
        password=request.POST['']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have login succesfully!')
            return redirect('home')
        else:
            messages.success(request,'We could not find an account with that username. Try another, or get a new account')
            return redirect('home')
        
    else:
        return render(request,'home.html')

    return render(request,'home.html')