from buakpsi.views import render_page
from django.template.loader import render_to_string
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