from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.
def home(request,*args, **kwargs):
    car_featuers = Car.objects.order_by('-created_at').filter(is_featured=True)
    teams = Team.objects.all()
    all_cars = Car.objects.order_by('-created_at')
    return render(request, 'pages/home.html',{
        'teams': teams,
        'car_featuers': car_featuers,
        'all_cars': all_cars
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