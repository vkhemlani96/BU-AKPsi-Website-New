from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.shortcuts import render
from django.core.mail import EmailMessage
from buakpsi.models import FAQ
from brothers.models import EBoardMember

def render_page(request, context, navbar_size = 'small'):
	context['navbar'] = navbar(navbar_size)
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
	context = {
		'body': render_to_string('buakpsi/index.html'),
		'post_body_script': render_to_string('buakpsi/index.js'),
	}

	return render_page(request, context, navbar_size='large')

def about(request):
	context = {
		'body': render_to_string('buakpsi/about.html')
	}

	return render_page(request, context)

def faq(request):

	body_context = {
		'FAQ': FAQ.objects.all(),
	}

	context = {
		'body': render_to_string('buakpsi/faq.html', body_context),
	}
	return render_page(request,context)


def contact(request):

	email_sent = False

	if request.method == 'POST':
		# Emails are sent to president, evp and akpsi.nu.chapter@gmail.com email
		eboard_emails = EBoardMember.objects.all()[:2].values_list('brother__email', flat=True)
		to_emails = ['akpsi.nu.chapter@gmail.com'] + ["%s@bu.edu" % x for x in eboard_emails]
		print(to_emails)

		email = EmailMessage(
			request.POST['messageSubject'],
			"Sender: %s (%s)\r\n\r\nMessage:\r\n%s"
				% (request.POST['messageName'], request.POST['messageEmail'], request.POST['message']),
			'AKPsi - Website Contact Form <akpsi.nu.chapter@gmail.com>',
			to_emails,
			reply_to=[request.POST['messageEmail']],
		)
		email.send()
		email_sent = True

	context = {
		'body': render_to_string('buakpsi/contact.html', context={'email_sent': email_sent}, request=request),
		'post_body_script': render_to_string('buakpsi/contact.js'),
		'head': render_to_string('buakpsi/contact_head.html'),
	}
	return render_page(request, context, navbar_size='large')