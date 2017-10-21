from django.db import models
from django.db.models import Case, When, Value, IntegerField
from brothers.models import Brother
from buakpsi.models import PositionManager

class NCCGManager(PositionManager):
    positions = [
        'Executive Director',
        'Engagement Manager',
        'Senior Associate',
        'Associate'
    ]

class NCCGMember(models.Model):
    # Order is done through sorting in view
    brother = models.OneToOneField(Brother)
    position = models.CharField(max_length=45)
    bio = models.TextField()
    objects = NCCGManager()

    def __str__(self):
        return "%s %s (%s)" % (self.brother.first_name, self.brother.last_name, self.position)

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"