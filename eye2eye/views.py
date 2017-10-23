from eye2eye.models import Eye2EyeMember, BlogArticle
from buakpsi.views import render_page
from django.template.loader import render_to_string

def index(request):
	body_context = {
		'articles': BlogArticle.objects.all()[:2],
	}

	context = {
		"body": render_to_string("eye2eye/index.html", body_context),
	}
	return render_page(request, context)

def board(request):
	body_context = {
		'members': Eye2EyeMember.objects.all(),
	}

	context = {
		"body": render_to_string("eye2eye/board.html", body_context),
		"post_body_script": render_to_string("eye2eye/board.js")
	}
	return render_page(request, context)

def blog(request):
	body_context = {
		'articles': BlogArticle.objects.all()[:10],
	}

	context = {
		"body": render_to_string("eye2eye/blog.html", body_context),
		# "post_body_script": render_to_string("eye2eye/board.js")
	}
	return render_page(request, context)

def article(request, slug):
	body_context = {
		'article': BlogArticle.objects.get(slug=slug),
	}

	context = {
		"body": render_to_string("eye2eye/blog.html", body_context),
		# "post_body_script": render_to_string("eye2eye/board.js")
	}
	return render_page(request, context)