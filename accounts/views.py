from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User


def login(request, *args, **kwargs):
    return render(request, 'accounts/login.html')


def logout(request, *args, **kwargs):
    return render(request, 'accounts/logout.html')


def register(request, *args, **kwargs):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            pass
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User is already exists')
                return redirect('account:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is alredy exists')
                    return redirect('account:register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname,
                                                    email=email,username=username,password=password)
                    user.save()
                    auth.login(request,user)
                    messages.success(request, 'Your are now logged in.')
                   
                    return redirect('account:dashboard')
                
                    
        
    else:
        return render(request, 'accounts/register.html')


def dashboard(request, *args, **kwargs):
    return render(request, 'accounts/dashboard.html')
