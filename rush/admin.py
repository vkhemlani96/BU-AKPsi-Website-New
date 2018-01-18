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

class RushProfileAdmin(admin.ModelAdmin):
	list_display = ('name', 'semester', 'majors', 'grade')
	list_display = ('name',)

	def name(self, obj):
		return "%s %s" % (obj.first_name, obj.last_name)

	def semester(self, obj):
		semester_full = "Fall" if obj.semester[0] == "F" else "Spring"
		year_full = "20" + obj[1:]
		return "%s %s" % (semester_full, year_full)

admin.site.register(RushEvent, EventAdmin)
admin.site.register(RushEventLocation, EventLocationAdmin)
admin.site.register(RushProfile, RushProfileAdmin)