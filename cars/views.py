from django.shortcuts import render, get_object_or_404
from . models import Car
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

# Create your views here.


def cars(request, *args, **kwargs):
    all_cars = Car.objects.order_by('-created_at')
    paginator = Paginator(all_cars, 3)
    page = request.GET.get('page')
    paged_car = paginator.get_page(page)
    # seach field
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()

    return render(request, 'cars/car.html', {
        'all_cars': paged_car,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search
    })


def car_detail(request, value_from_url, *args, **kwargs):
    car_details = get_object_or_404(Car, id=value_from_url)
    data = {
        'car_details': car_details
    }
    return render(request, 'cars/car_details.html', data)


def search(request, *args, **kwargs):

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()
    
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    all_cars = Car.objects.order_by('-created_at')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            all_cars = all_cars.filter(description__icontains=keyword)

    elif 'model' in request.GET:
        model = request.GET['model']
        if model:
            all_cars = all_cars.filter(model__iexact=model)

    elif 'city' in request.GET:
        city = request.GET['city']
        if city:
            all_cars = all_cars.filter(city__iexact=city)

    elif 'year' in request.GET:
        year = request.GET['year']
        if year:
            all_cars = all_cars.filter(year__iexact=year)

    elif 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            all_cars = all_cars.filter(body_style__iexact=body_style)

    elif 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            all_cars = all_cars.filter(
                price__gte=min_price, price__lte=max_price)

    context = {
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search':transmission_search
    }
    return render(request, 'cars/search.html', context)
