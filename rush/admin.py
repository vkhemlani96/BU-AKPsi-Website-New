from django.contrib import admin
from .models import *
from buakpsi.models import rush_FAQ

class RushFAQAdmin(admin.ModelAdmin):
	list_display = ('question', )
	list_display_links = ('question',)

class EventLocationAdmin(admin.ModelAdmin):
	list_display = ('name', 'abbreviation', 'lat', 'lng')
	list_display_links = ('name',)

class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'location', 'start_time', 'end_time', 'is_open_rush')
	list_display_links = ('name',)

	def location(self, obj):
		return "%s %s" % (obj.building.abbreviation, obj.room_number)

class RushProfileAdmin(admin.ModelAdmin):
	list_display = ('name', 'email_appended', ('semester_year'), 'majors', 'grade')
	list_display_links = ('name',)

	def name(self, obj):
		return "%s %s" % (obj.first_name, obj.last_name)

	def email_appended(self, obj):
		return "%s@bu.edu" % (obj.email)
	email_appended.short_description = "Email"

	def semester_year(self, obj):
		semester_full = "Fall" if obj.semester[0] == "F" else "Spring"
		year_full = "20" + obj.semester[1:]
		return "%s %s" % (semester_full, year_full)
	semester_year.short_description = "Semester"

	name.admin_order_field = 'name'

class RushApplicationAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_display_links = ('name',)

	def name(self, obj):
		rush = obj.profile
		return "%s %s" % (rush.first_name, rush.last_name)

	def URL(self,obj):
		return "http://www.buakpsi.com/"

admin.site.register(rush_FAQ, RushFAQAdmin)
admin.site.register(RushEvent, EventAdmin)
admin.site.register(RushEventLocation, EventLocationAdmin)
admin.site.register(RushProfile, RushProfileAdmin)
admin.site.register(RushApplication, RushApplicationAdmin)