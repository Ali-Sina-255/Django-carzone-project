from django.contrib import admin
from . models import Team
from django.utils.html import format_html
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
	def thumbinail(self, object):
		return format_html('<img src="{}" width="40" style="border-radius:50px" />'.format(object.photo.url))
	list_display = ('id', 'first_name', 'last_name',
					'thumbinail', 'designation', 'created_time')
	list_display_links = ('id', 'thumbinail', 'first_name')
	search_fields = ('first_name', 'last_name')


admin.site.register(Team, TeamAdmin)
