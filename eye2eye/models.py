from django.db import models
from buakpsi.models import PositionManager
from brothers.models import Brother

class Eye2EyeManager(PositionManager):
  positions = [
      "President",
      "Vice President",
      "Director of Finance",
      "Director of Research",
      "Director of Operations",
      "Director of Marketing",
      "Director of Public Relations"
  ]

class Eye2EyeMember(models.Model):
    brother = models.OneToOneField(Brother)
    position = models.CharField(max_length=45)
    bio = models.TextField()
    objects = Eye2EyeManager()

    def __str__(self):
        return "%s %s (%s)" % (self.brother.first_name, self.brother.last_name, self.position)

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"