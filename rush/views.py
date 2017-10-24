from django.shortcuts import render
from django.template.loader import render_to_string
from buakpsi.views import render_page
from rush.models import RushEventLocation, RushEvent

def index(request):

	events = RushEvent.objects.filter(is_open_rush = True)
	building_ids = events.values_list('building', flat=True)
	buildings = RushEventLocation.objects.filter(pk__in=building_ids).distinct()

	print(buildings)

	body_context = {
	}
	
	context = {
		"body": render_to_string("rush/index.html", body_context),
	}
	return render_page(request, context)