from django.db import models
from django.contrib.postgres import fields

class RushEventLocation(models.Model):
	name = models.CharField(max_length=50)
	abbreviation = models.CharField(
		max_length=5,
		blank=True,
		help_text='Leave blank for something like "BU Beach"')
	lat = models.DecimalField(
		decimal_places=6,
		max_digits=8,
		verbose_name='Latitude',
		help_text='Put building name into https://www.latlong.net/ for lat/lng')
	lng = models.DecimalField(
		decimal_places=6,
		max_digits=8,
		verbose_name='Longitude',
		help_text='See above')

	class Meta:
		verbose_name='Event Location'
		ordering=['name']

	def __str__(self):
		if len(self.abbreviation):
			return "%s (%s)" % (self.name, self.abbreviation.upper())
		else:
			return "%s" % (self.name)

class RushEvent(models.Model):
	name = models.CharField(max_length=50)
	building = models.ForeignKey(RushEventLocation)
	room_number = models.CharField(
		max_length=20,
		blank=True,
		verbose_name='Room Number or Name',
		help_text='Ex. "Backcourt" for GSU Backcourt or "209" for PHO 209')
	room_long_name = models.CharField(
		max_length=50,
		blank = True,
		verbose_name='Room Name (Long)',
		help_text='Example: Photonics Center Auditorium (for PHO 206)')
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	description = models.TextField(
		help_text='Use HTML tags to bold or italicize text.'
			'<br>Note: Use the same description for both infosessions.')
	is_open_rush = models.BooleanField(verbose_name='Open Rush?')

	class Meta:
		verbose_name='Event'
		ordering = ['start_time']

	def __str__(self):
		return self.name

	def location(self):
		location = ""
		if len(self.building.abbreviation):
			location = self.building.abbreviation
		else:
			location = self.building.name

		if len(self.room_number):
			location += " " + self.room_number

		if len(self.room_long_name):
			location += " (" + self.room_long_name + ")"

		return location

class RushProfile(models.Model):
	FRESHMAN = "FR"
	SOPHOMORE = "SO"
	JUNIOR = "JR"
	SENIOR = "SR"

	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.CharField(max_length=8)
	semester = models.CharField(max_length=3)
	phone_number = models.CharField(max_length=11)
	grade = models.CharField(
		max_length=2, choices=((FRESHMAN, "Freshman"), (SOPHOMORE, "Sophomore"), (JUNIOR, "Junior"), (SENIOR, "Senior")))
	channel = models.CharField(max_length=30)

	major_schools = fields.ArrayField(models.CharField(max_length=3)) # max_length => CAS,ENG,QST
	majors = models.CharField(max_length=100)
	minors = models.CharField(max_length=100, blank = True, null = True)
	
	events_attended = fields.ArrayField(models.CharField(max_length=50), default = list)
	submitted_application = models.BooleanField(default = False)
	interview_wave = models.PositiveSmallIntegerField(null = True)
	interview_prelim_yes = models.PositiveSmallIntegerField(null = True)
	interview_prelim_no = models.PositiveSmallIntegerField(null = True)
	interview_prelim_abstain = models.PositiveSmallIntegerField(null = True)
	interview_prelim_deliberate = models.NullBooleanField(null = True)
	interview_final_yes = models.PositiveSmallIntegerField(null = True)
	interview_final_no = models.PositiveSmallIntegerField(null = True)
	interview_final_abstain = models.PositiveSmallIntegerField(null = True)
	given_bid = models.NullBooleanField(null = True)

class RushApplication(models.Model):
	profile = models.OneToOneField(RushProfile, on_delete=models.CASCADE, related_name='application')
	timestamp = models.DateTimeField(auto_now_add=True)
	address = models.CharField(max_length=15)
	gpa = models.CharField(max_length=5)
	application_answers = fields.JSONField()
	picture = models.ImageField(upload_to = 'rush_pics/', null = True)
	resume = models.FileField(upload_to = 'rush_resumes/', null = True)
