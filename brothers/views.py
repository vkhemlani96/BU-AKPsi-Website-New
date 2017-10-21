from buakpsi.views import render_page
from django.template.loader import render_to_string
from django.db.models import Max, Min
from .models import EBoardMember, Brother

def index(request):

	body_context = {
		'eboard': EBoardMember.objects.all().order_by("order"),
		'brothers': Brother.objects.filter(status = Brother.ACTIVE).order_by("last_name"),
		'active_classes': ["Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Transfer"]
	}
	
	context = {
		"body": render_to_string("brothers/index.html", body_context),
		"post_body_script": render_to_string("brothers/index.js")
	}
	return render_page(request, context)

def alumni(request):

	alumni_brothers = Brother.objects.filter(status = Brother.ALUMNI)
	years = alumni_brothers.aggregate(Max('year'), Min('year'))
	min_year = int(years['year__min'])
	max_year = int(years['year__max'])
	alumni = dict()

	for year in range(min_year, max_year+1):
		brothers = alumni_brothers.filter(year = str(year))
		alumni[year] = brothers

	body_context = {
		'active_brothers': alumni,
		'min_year': min_year,
		'max_year': max_year,
		'years': range(min_year, max_year+1),
	}

	js_context = {
		'min_year': min_year,
		'max_year': max_year,
		'total_alumni': alumni_brothers.count(),
	}

	print(js_context)

	context = {
		"body": render_to_string("brothers/alumni.html", body_context),
		"post_body_script": render_to_string("brothers/alumni.js", js_context)
	}

	return render_page(request, context)
