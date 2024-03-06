from django.contrib import admin
from . models import Car
from django.utils.html import format_html


class CarAdmin(admin.ModelAdmin):
	def thumbinail(self, object):
		return format_html('<img src="{}" width="40" style="border-radius:50px" />'.format(object.car_photo.url))
	
	list_display = ('id','thumbinail','cart_title','city','color','model','year','body_style','fuel_type','is_featured')
	list_display_links = ('id','cart_title')
	list_editable = ('is_featured',)
	search_fields = ('cart_title','city','body_style','model','fuel_type')
	list_filter = ('cart_title','city','body_style','model')
	
admin.site.register(Car, CarAdmin)
