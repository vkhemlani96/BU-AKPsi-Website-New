from nccg.models import SFGMember
from buakpsi.views import render_page
from django.template.loader import render_to_string
from django.shortcuts import render

def index(request):
	body = render_to_string('sfg/index.html')
	context = {
		'body': body,
	}

	return render_page(request, context)

def team(request):
	body_context = {
		'members': SFGMember.objects.all(),
	}

	context = {
		"body": render_to_string("sfg/team.html", body_context),
		"post_body_script": render_to_string("sfg/team.js")
	}
	return render_page(request, context)


