from django.shortcuts import render
from .models import Team
from cars.models import Car


def home(request, *args, **kwargs):
    car_featuers = Car.objects.order_by('-created_at').filter(is_featured=True)
    teams = Team.objects.all()
    all_cars = Car.objects.order_by('-created_at')
    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style')
    model_search = Car.objects.values_list('model',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    

    return render(request, 'pages/home.html', {
        'teams': teams,
        'car_featuers': car_featuers,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search':year_search,
        'body_style_search':body_style_search
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
