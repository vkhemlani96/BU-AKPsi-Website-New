from buakpsi.views import render_page
from django.template.loader import render_to_string
from django.db.models import Max, Min
from .models import EBoardMember, Brother

classes = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", 
	"Zeta", "Eta", "Theta", "Iota", "Kappa", "Lambda", "Mu",
	"Nu", "Xi", "Omicron", "Pi", "Rho", "Sigma", "Tau", "Upsilon",
	"Phi", "Chi", "Psi", "Omega"]

# Calculates score for class used to sort
# Alpha: 0
# Beta: 1
# ...
# Alpha Alpha: 24
# Alpha Beta: 25 ...
def key_for_class(class_name): 
	letters = class_name.split(' ')
	return sum(i*len(classes) + classes.index(letters[i]) for i in range(len(letters)))

def index(request):

	brothers = Brother.objects.filter(status = Brother.ACTIVE).order_by("last_name")
	classes = set(brothers.values_list('class_name', flat=True)\
		.exclude(class_name = "Transfer"))
	sorted_classes = sorted(classes, key=key_for_class) + ["Transfer"]

	print(sorted_classes)

	body_context = {
		'eboard': EBoardMember.objects.all(),
		'brothers': brothers,
		'active_classes': sorted_classes
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
