from django.contrib import admin
from . models import Contact


class AdminContact(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name','email','city','car_title','created_at')
    list_display_links = ('id','first_name', 'last_name')
    search_fields = ('fist_name','last_name','car_title')
    list_per_page = 20
    
admin.site.register(Contact, AdminContact)