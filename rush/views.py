from django.shortcuts import render
from django.utils.html import format_html
from django.template.loader import render_to_string
from buakpsi.views import render_page
from rush.models import RushEventLocation, RushEvent, RushProfile
from rush.settings import SIGNUP_SOURCES, SEMESTER

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

	center = {}
	if len(events):
		center = {
			'lat': sum([building.lat for building in buildings]) / buildings.count(),
			'lng': sum([building.lng for building in buildings]) / buildings.count(),
		}
	else:
		center = {
			'lat': 42.350500,
			'lng': -71.105399
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
	}
	return render_page(request, context)

def signup(request, src):
	if not src:
		text = ""
		for source in SIGNUP_SOURCES:
			text += '<p><a href="./%s">%s</a></p>' % (source, source)

		context = {
			"body": format_html(text),
		}

		return render_page(request, context)

	else:
		if request.method == "GET":
			context = {
				"body": render_to_string('rush/signup.html', {"title": src}, request=request),
				"post_body_script": render_to_string('rush/signup.js')
			}

			return render_page(request, context)

		elif request.method == "POST":

			data = request.POST
			print(data)
			for key in data.keys():
				print(key, data.getlist(key))
			rush = RushProfile(
				first_name = data.get('rushFirstName'),
				last_name = data.get('rushLastName'),
				email = data.get('rushEmail').replace("@bu.edu",""),
				semester = SEMESTER,
				phone_number = data.get('rushPhone'),
				grade = data.get('rushGrade'),
				channel = src,

				major_schools = data.getlist('rushSchool[]'),
				majors = data.get('rushMajors'),
				minors = data.get('rushMinors')
			)

			success_error_msg = "%s has successfully been signed up" % (data.get('rushFirstName'),)
			try:
				rush.save()
			except Exception:
				success_error_msg = "An error has occurred. Please try again."

			body_context = {
				'title': src,
				'success_error_msg': success_error_msg
			}
			context = {
				"body": render_to_string('rush/signup.html', body_context, request=request),
				"post_body_script": render_to_string('rush/signup.js')
			}
			return render_page(request, context)