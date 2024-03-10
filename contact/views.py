from django.shortcuts import render, redirect
from . models import Contact
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.models import User



def inquiry(request, *args, **kwargs):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'you already make an enquriy about this car.Please wait until we get back to you.')
                return redirect('cars')
        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        
        email = EmailMessage(
            "New Car Inquiry",
            "Have a new inquiry for the car " + car_title + ".please login to admin panel for more info.",
            "alisiansultani52@gmail.com",
            [admin_email],
            fail_silently=False
        )
        contact_inventoru = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name,
                                    last_name=last_name, customer_need=customer_need, city=city, state=state, email=email, phone=phone, message=message)
        contact_inventoru.save()
        messages.success(
            request, 'Your request has been submitted, we will get back you shortly.')
        return redirect('pages:home')
    else:
        messages.error(request, 'message is not save in to the databases.')
        return redirect('pages:home')
