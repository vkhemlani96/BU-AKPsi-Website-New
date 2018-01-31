from buakpsi.views import render_page
from django.template.loader import render_to_string
from rush.models import RushProfile
from rush.settings import SEMESTER
from random import shuffle

class ShortAnswerQuestion():

	def __init__(self, question, required = True):
		self.question = question
		self.required = required

class LogicQuestion():

	def __init__(self, question, answer = None, input_type = "multiple_choice", options = None, image = None):
		self.question = question
		self.input_type = input_type
		self.answer = answer
		self.image = image
		self.options = options

		if options:
			shuffle(self.options)

QUESTIONS = {
	"short_answer": [
		ShortAnswerQuestion("Why Alpha Kappa Psi?"),
		ShortAnswerQuestion("What is your most notable work/leadership experience?"),
		ShortAnswerQuestion("You are disappointed about an unfair decision. How do you react?"),
		ShortAnswerQuestion("How do you know that you are stressed? What do you to de-stress?"),
		ShortAnswerQuestion("<i>If this is not your first time applying</i>, what have you done to strengthen your candidacy?", required = False),
	],
	"feedback": [
		ShortAnswerQuestion("Feel free to include any feedback you may have regarding the open rush events:", required = False),
	],
	"logic": [
		LogicQuestion(
			"""I. Esther is older than Katherine<br>
				II. Ashley is older than Esther<br>
				III. Katherine is younger than Ashley<br><br>
			
				If the first two statements are true, then the third statement is:""",
			"True",
			options = [
				"True",
				"False",
				"Uncertain"
			]
		),
		LogicQuestion(
			"""Here are some words translated from an artificial language.<br>
				I. \"slar\" means \"jump\"<br>
				II. \"slary\" means \"jumping\"<br>
				III. \"slarend\" means \"jumped\"<br><br>
				Which word could mean \"playing\"?""",
			"Clargy",
			options = [
				"Clargslarend",
				"Clargy",
				"Ellaclarg",
				"Slarmont"
			]
		),
		LogicQuestion(
			"""If LIGHT is coded as GILTH, find the code for RAINY.""",
			"IARYN",
			options = [
				"IARYN",
				"RINAY",
				"IARNY",
				"ARINY"
			]
		),
		LogicQuestion(
			"""Which one is heavier, a pound of steel or a pound of tea?""",
			"Neither",
			options = [
				"Steel",
				"Tea",
				"Neither"
			]
		),
		LogicQuestion(
			"""Fill in the blank: LKJ, MIH, NGF, ___, PCB:""",
			"OED",
			options = [
				"CMN",
				"OED",
				"OAT",
				"XYQ"
			]
		),
		LogicQuestion(
			"""Divide 30 by half, add 10. What is the answer?""",
			"70",
			options = [
				"25",
				"20",
				"70"
			]
		),
		LogicQuestion(
			"""A farmer has 12 horses, all but 7 die. How many does he have left?""",
			answer = "7",
			input_type = "number",
		),
		LogicQuestion(
			"""In three years Eric will be thrice as old as he was five years ago. How old is he today?""",
			answer = "9",
			input_type = "number",
		),
		LogicQuestion(
			"""A spider is at the bottom of a 30 meter well. He jumps once everyday and rises 3 meters up the well.
			While he is asleep, he slips 2 meters downwards. How many days does it take him to escape the well?""",
			answer = "28",
			input_type = "number",
		),
		LogicQuestion(
			"""A spider is at the bottom of a 30 meter well. He jumps once everyday and rises 3 meters up the well.
			While he is asleep, he slips 2 meters downwards. How many days does it take him to escape the well?""",
			answer = "28",
			input_type = "number",
		),
		LogicQuestion(
			"""Please solve the riddle above.""",
			answer = "52",
			input_type = "number",
			image = "logic_shape_math.png",
		),

	]

}

def index(request):
	script_context = {
		"rushes": RushProfile.objects.filter(semester = SEMESTER)
	}
	
	context = {
		"body": render_to_string("rush/application.html", {"questions": QUESTIONS}),
		"head": render_to_string("rush/application_head.html"),
		"post_body_script": render_to_string("rush/application.js", script_context),
	}
	return render_page(request, context)