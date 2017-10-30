from django.shortcuts import render
from django.template.loader import render_to_string
from buakpsi.views import render_page
from rush.models import RushEventLocation, RushEvent

def index(request):

	events = RushEvent.objects.filter(is_open_rush = True).order_by('start_time')
	building_ids = events.values_list('building', flat=True)
	buildings = RushEventLocation.objects.filter(pk__in=building_ids).distinct()

	markers = {}
	for building in buildings:
		markers[building] = {}

	# Organize events by buildings
	for event in events:
		building = markers[event.building]
		room = event.room_number
		if event.room_long_name:
			room += " (%s)" % event.room_long_name
		if room in building.keys():
			building[room] += ', ' + event.name
		else:
			building[room] = event.name

	# Turn building rooms and events into string
	for building in buildings:
		window_text = []
		for room in markers[building].keys():
			window_text.append("<strong>%s</strong>" % markers[building][room])
			window_text.append(room)
		markers[building] = "<br>".join(window_text)

	center = {
		'lat': sum([building.lat for building in buildings]) / buildings.count(),
		'lng': sum([building.lng for building in buildings]) / buildings.count(),
	}

	body_context = {
		"markers": markers,
		"center": center,
		"events": events,
		"from_facebook": 'HTTP_REFERER' in request.META.keys() and 'facebook' in request.META['HTTP_REFERER']
	}
	
	context = {
		"head": render_to_string("rush/index_head.html"),
		"body": render_to_string("rush/index.html", body_context),
		# "post_body_script": render_to_string("rush/index.js"),
	}
	return render_page(request, context)