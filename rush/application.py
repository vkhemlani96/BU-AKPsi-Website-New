import traceback
from buakpsi.views import render_page
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from rush.models import RushProfile, RushApplication
from rush.settings import SEMESTER
from random import shuffle

class ShortAnswerQuestion():

	def __init__(self, question, required = True):
		self.question = question
		self.required = required

class LogicQuestion():

	def __init__(self, question, answer = None, input_type = "multiple_choice", options = None, image = None):
		self.question = question
		self.answer = answer
		self.input_type = input_type
		self.image = image
		self.options = options

		if options:
			shuffle(self.options)

QUESTIONS = {
	"short_answer": [
		ShortAnswerQuestion("Why Alpha Kappa Psi?"),
		ShortAnswerQuestion("What is your most notable work/leadership experience?"),
		ShortAnswerQuestion("You are disappointed about an unfair decision. How do you react?"),
		ShortAnswerQuestion("How do you know that you are stressed? What do you do to de-stress?"),
		ShortAnswerQuestion("<i>If this is not your first time applying</i>, what have you done to strengthen your candidacy?", required = False),
	],
	"logic": [
		LogicQuestion("""Jack is an apple farmer. His farm usually produces 4 apples per year, 1 of which he gives it to his family. Each apple weighs 100 grams. This year, he had an amazing yield of 6 apples and 4 blueberries. However the apples were small and weighed only 50 grams each. He can sell his apples for $0.40 a gram. If it wasn't an unusual yield and he sold all his apple yields, how much revenue did Jack make last year?""",
			"160",
			input_type = "number",
		),
		LogicQuestion("""Neil owns a factory which produces parts of toy cars. The toy car is made up of 4 tires, 4 bearings, a plastic cover and a motor. Neil's factory exclusively produces 16,000 tires, 1,600 bearings and 100 motors a day. If Neil only uses the parts produced at his factory within the course of 5 days, how many toy cars can Neil produced?""",
			"0",
			input_type = "number",
		),
		ShortAnswerQuestion("""How many tennis balls can you fit in a BU shuttle bus? Explain the thought process you went through to get the answer.""",
		),
	],
	"feedback": [
		ShortAnswerQuestion("Feel free to include any feedback you may have regarding the open rush events:", required = False),
	],

}

def index(request):
	script_context = {
		"rushes": RushProfile.objects.filter(semester = SEMESTER)
	}
	
	context = {
		"body": render_to_string("rush/application.html", {"questions": QUESTIONS}, request=request),
		"head": render_to_string("rush/application_head.html"),
		"post_body_script": render_to_string("rush/application.js", script_context),
	}
	return render_page(request, context)

def submit(request):

	success = False
	failure_data = None
	try:
		application_answers = {}
		post_data = request.POST
		for key in post_data:
			if "short_answer_" in key or "feedback_" in key or "logic_" in key:
				application_answers[key] = post_data.get(key)

		email = post_data.get('rushEmail').replace("@bu.edu","")
		rush = None
		matchingRushes = RushProfile.objects.filter(email = email)

		if matchingRushes.count() > 0:
			rush = matchingRushes[0]
			rush.channel = 'application'
		else:
			rush = RushProfile()

		rush.first_name = post_data.get('rushFirstName')[:20]
		rush.last_name = post_data.get('rushLastName')[:20]
		rush.email = email
		rush.semester = SEMESTER
		rush.phone_number = post_data.get('rushPhone')[:11]
		rush.grade = post_data.get('rushGrade')
		rush.major_schools = post_data.getlist('rushSchool[]')
		rush.majors = post_data.get('rushMajors')[:100]
		rush.minors = post_data.get('rushMinors')[:100]
		rush.submitted_application = True

		application = RushApplication(
			profile = rush,
			address = post_data.get('rushAddress')[:30],
			gpa = post_data.get('rushGPA')[:5],
			application_answers = application_answers,
			picture = request.FILES['rushPic'],
			resume = request.FILES['rushResume'],
		)

		email = EmailMessage(
			"Alpha Kappa Psi - Rush Application Submission",
			"Dear " + post_data['rushFirstName'] + ",\r\n\r\nThank you for your application! We look forward to reviewing your application and will contact you with further details on your candidacy by Sunday night. Below is a copy of your application for your own record.\r\n\r\n------------------------------\r\n\r\n" + 
					"Email: " + post_data.get("rushEmail") + "@bu.edu\r\n" + 
					"First Name: " + post_data.get("rushFirstName") + "\r\n" +
					"Last Name: " + post_data.get("rushLastName") + "\r\n" +
					"Grade: " + post_data.get("rushGrade") + "\r\n" +
					"School: " + str(post_data.getlist("rushSchool[]")) + "\r\n" +
					"Majors: " + post_data.get("rushMajors") + "\r\n" +
					"Minors: " + post_data.get("rushMinors") + "\r\n" +
					"Phone: " + post_data.get("rushPhone") + "\r\n" +
					"Address: " + post_data.get("rushAddress") + "\r\n" +
					"GPA: " + post_data.get("rushGPA") + "\r\n"+ "\r\n" +
					"Answers: " + str(application_answers) + "\r\n"+ "\r\n",
			'Alpha Kappa Psi Nu Chapter <akpsi.nu.chapter@gmail.com>',
			to=[email+"@bu.edu"],
			reply_to=["akpsi.nu.recruitment@gmail.com"],
		)
		print("test")
		email.send()
		application.save()
		success = True

	except Exception as e:
		traceback.print_exc()
		failure_data = str(request.POST) + """

		%s """ % str(e)

	body_context = {
		"success": success,
		"failure_data": failure_data
	}
	context = {
		"body": render_to_string("rush/submit.html", body_context, request=request),
	}

	return render_page(request, context)