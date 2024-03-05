from django.shortcuts import render

# Create your views here.
def cars(request, *args, **kwargs):
    return render(request, 'cars/car.html')