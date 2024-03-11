from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contact.models import Contact
from django.contrib.auth.decorators import login_required


def login(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in now')
            return redirect('account:dashboard')
        else:
            messages.error(request, 'invalid Logged in credentail!!')
            return redirect('account:login')
    return render(request, 'accounts/login.html')


def logout(request, *args, **kwargs):
    auth.logout(request)
    messages.success(request, 'You are now logout!!!')
    return redirect('pages:home')
    # if request.method == 'POST':
    #     auth.logout(request)
    #     messages.success(request, 'You are now logout!!!')
    #     return redirect('pages:home')
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
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User is already exists')
                return redirect('account:register')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is alredy exists')
                    return redirect('account:register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname,
                                                    email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'Your are now logged in.')
                    user.save()
                    return redirect('account:dashboard')
                    # user.save()
                    # messages.success(request, 'you are logged in now')
                    # return redirect('account:login')
        else:
            messages.error(request, 'passowrd dont match')
            return redirect('account:register')
    return render(request, 'accounts/register.html')


@login_required(login_url='account:login')
def dashboard(request, *args, **kwargs):
    user_inquriy = Contact.objects.order_by(
        'created_at').filter(user_id=request.user.id)
    context = {
        'user_inquriy': user_inquriy,
    }
    return render(request, 'accounts/dashboard.html', context)
