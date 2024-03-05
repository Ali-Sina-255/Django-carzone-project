from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request,*args, **kwargs):
    teams = Team.objects.all()
    return render(request, 'pages/home.html',{
        'teams': teams
    })


def about(request, *args, **kwargs):
    teams = Team.objects.all()
    data = {
        'teams': teams
    }
    return render(request, 'pages/about.html', data)



def services(request, *args, **kwargs):
    return render(request, 'pages/services.html')



def contact(request, *args, **kwargs):
    return render(request, 'pages/contact.html')