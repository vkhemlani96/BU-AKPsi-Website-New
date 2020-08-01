from django.db import models
from django.db.models import Case, When, Value, IntegerField
from brothers.models import Brother
from buakpsi.models import PositionManager

class SFGManager(PositionManager):
    positions = [
        'President',
        'Co-President',
        'VP of Education',
        'VP of Corporate Relations',
        'Senior Associate',
        'Associate',
        'Analyst',
    ]

class SFGMember(models.Model):
    brother = models.OneToOneField(Brother)
    position = models.CharField(max_length=45)
    bio = models.TextField()
    objects = SFGManager()

    def __str__(self):
        return "%s %s (%s)" % (self.brother.first_name, self.brother.last_name, self.position)

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"

    def name(self):
        return "%s %s" % (self.brother.first_name, self.brother.last_name)

