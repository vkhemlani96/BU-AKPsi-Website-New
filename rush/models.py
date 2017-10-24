from django.db import models

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