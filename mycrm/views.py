from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
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

#log out function
def logout_user(request):
    logout(request)
    messages.success(request,'You have been logout Successfully')
    return redirect('home')

# Register Function
def Register_user(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        password1=request.POST['password1']
        password2=request.POST['password2']
        if form.is_valid():
            form.save()
            messages.success(request,'You have successfully Registered!')
            return redirect('home')
        elif password1!= password2:
            messages.success(request,'Your password and confirm password are not same!')
            return redirect('Register')
    else:
        form=SignUpForm()
        return render(request,'Register.html',{'form':form})
    return render(request,'Register.html')

