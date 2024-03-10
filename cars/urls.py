from django.urls import path
from . import views

# app_name = 'car'

urlpatterns = [
    path('', views.cars, name='cars'),
    path('car-details/<int:value_from_url>/', views.car_detail, name='car-details'),
    path('search', views.search, name='search')
]
