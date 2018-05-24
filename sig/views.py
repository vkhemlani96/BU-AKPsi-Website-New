from nccg.models import NCCGMember, NCCGAdvisor, NCCGPartner, NCCGClient
from buakpsi.views import render_page
from django.template.loader import render_to_string
from django.shortcuts import render

def index(request):
	body = render_to_string('nccg/index.html')
	context = {
		'body': body,
	}

	return render_page(request, context)

def team(request):
	body_context = {
		'members': NCCGMember.objects.all(),
	}

	context = {
		"body": render_to_string("nccg/team.html", body_context),
		"post_body_script": render_to_string("nccg/team.js")
	}
	return render_page(request, context)

def advisors(request):
	body_context = {
		'advisors': NCCGAdvisor.objects.all(),
	}

	context = {
		"body": render_to_string("nccg/advisors.html", body_context),
	}
	return render_page(request, context)

def partners(request):
	body_context = {
		'partners': NCCGPartner.objects.all(),
	}

	context = {
		"body": render_to_string("nccg/partners.html", body_context),
	}
	return render_page(request, context)

def clients(request):
	body_context = {
		'clients': NCCGClient.objects.all(),
	}

	context = {
		"body": render_to_string("nccg/clients.html", body_context),
	}
	return render_page(request, context)

