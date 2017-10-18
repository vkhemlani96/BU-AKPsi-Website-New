from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

def render_page(request, context, navbar_size = 'small'):
	context['navbar'] = navbar(navbar_size == 'small')
	return render(request, 'buakpsi/wrapper.html', context)

def navbar(small):
	context = dict()

	if small:
		context = {
			'navbar_class': 'navbar_small',
			'left': ["-20px", "-34px", "-24px"],
			'sep': False,
		}
	else:
		context = {
			'navbar_class': 'navbar',
			'left': ["426px", "647px", ""],
			'sep': True
		}

	return render_to_string('buakpsi/navbar.html', context)

def index(request):
	body = render_to_string('buakpsi/index.html')
	post_body_script = render_to_string('buakpsi/index.js')
	context = {
		'body': body,
		'post_body_script': post_body_script,
	}

	return render_page(request, context, navbar_size='large')