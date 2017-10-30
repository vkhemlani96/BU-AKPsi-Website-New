from django.contrib import admin
from .models import *

class EventLocationAdmin(admin.ModelAdmin):
	list_display = ('name', 'abbreviation', 'lat', 'lng')
	list_display_links = ('name',)

class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'location', 'start_time', 'end_time', 'is_open_rush')
	list_display_links = ('name',)

	def location(self, obj):
		return "%s %s" % (obj.building.abbreviation, obj.room_number)

admin.site.register(RushEvent, EventAdmin)
admin.site.register(RushEventLocation, EventLocationAdmin)