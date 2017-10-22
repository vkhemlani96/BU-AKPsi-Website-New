from eye2eye.models import Eye2EyeMember
from buakpsi.views import render_page
from django.template.loader import render_to_string

def board(request):

	body_context = {
		'members': Eye2EyeMember.objects.all(),
	}

	print(body_context['members'])
	
	context = {
		"body": render_to_string("eye2eye/board.html", body_context),
		"post_body_script": render_to_string("eye2eye/board.js")
	}
	return render_page(request, context)