import csv
from django.shortcuts import render
from django.utils.html import format_html
from django.template.loader import render_to_string
from django.http import HttpResponse
from buakpsi.views import render_page
from rush.models import RushEventLocation, RushEvent, RushProfile
from rush.settings import SIGNUP_SOURCES, SEMESTER, DATA_PASSWORD, EXPORT_PASSWORD

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

def event(request, name):
	if not name:
		text = ""
		events = RushEvent.objects.all().values_list('name', flat=True)
		for name in events:
			text += '<p><a href="./%s">%s</a></p>' % (name, name)

		context = {
			"body": format_html(text),
		}

		return render_page(request, context)

	else:
		rushes = RushProfile.objects.filter(semester=SEMESTER)
		if request.method == "GET":
			context = {
				"body": render_to_string('rush/events.html', {"title": name}, request=request),
				"post_body_script": render_to_string('rush/events.js', {"rushes": rushes})
			}

			return render_page(request, context)

		elif request.method == "POST":

			data = request.POST
			email = data.get('rushEmail').replace("@bu.edu","")
			rush = None
			matchingRushes = RushProfile.objects.filter(email = email)

			if matchingRushes.count() > 0:
				rush = matchingRushes[0]
				rush.channel = 'event'
			else:
				rush = RushProfile()

			rush.first_name = data.get('rushFirstName')
			rush.last_name = data.get('rushLastName')
			rush.email = email
			rush.semester = SEMESTER
			rush.phone_number = data.get('rushPhone')
			rush.grade = data.get('rushGrade')
			rush.major_schools = data.getlist('rushSchool[]')
			rush.majors = data.get('rushMajors')
			rush.minors = data.get('rushMinors')
			if not name in rush.events_attended:
				rush.events_attended.append(name)

			rush.save()

			success_error_msg = "%s %s - Saved Successfully" % (data.get('rushFirstName'),data.get('rushLastName'))
			try:
				rush.save()
			except Exception:
				success_error_msg = "An error has occurred. Please try again."

			body_context = {
				'title': name,
				'success_error_msg': success_error_msg
			}
			context = {
				"body": render_to_string('rush/events.html', body_context, request=request),
				"post_body_script": render_to_string('rush/events.js', {"rushes": rushes})
			}
			return render_page(request, context)

fields = (
	('First Name', 'first_name'),
	('Last Name', 'last_name'),
	('Email', 'email'),
	('Grade', 'grade'),
	('Channel', 'channel'),
	('Schools', 'major_schools'),
	('Majors', 'majors'),
	('Minors', 'minors'),
	('Events', 'events_attended'),
)

def export(request):
	if request.POST.get("password") != EXPORT_PASSWORD:
		body_context = {
			"incorrect_password": (request.POST.get("password") != None)
		}
		context = {
			"body": render_to_string('rush/data.html', body_context, request=request)
		}
		return render_page(request, context)


	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="rushes_%s.csv"' % SEMESTER

	writer = csv.writer(response)
	writer.writerow([x[0] for x in fields])

	rushes = RushProfile.objects.filter(semester = SEMESTER).values_list(*[x[1] for x in fields])

	for rush in rushes:
		writer.writerow([str(x) for x in rush])

	return response

def data(request):
	if request.POST.get("password") != DATA_PASSWORD:
		body_context = {
			"incorrect_password": (request.POST.get("password") != None)
		}
		context = {
			"body": render_to_string('rush/data.html', body_context, request=request)
		}
		return render_page(request, context)

	rushes = RushProfile.objects.all()
	

	context = {
		"body": render_to_string('rush/data.html', request=request)
	}
	return render_page(request, context)