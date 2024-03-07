from django.shortcuts import render, get_object_or_404
from . models import Car
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

# Create your views here.
def cars(request, *args, **kwargs):
    all_cars = Car.objects.order_by('-created_at')
    paginator = Paginator(all_cars,3)
    page = request.GET.get('page')
    paged_car = paginator.get_page(page)
    
    return render(request, 'cars/car.html',{
        'all_cars': paged_car
    })


def car_detail(request,value_from_url,*args, **kwargs):
    car_details = get_object_or_404(Car, id=value_from_url)
    data = {
        'car_details': car_details
    }
    return render(request, 'cars/car_details.html', data)