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
    brother = models.OneToOneField(Brother)
    position = models.CharField(max_length=45)
    bio = models.TextField()
    objects = NCCGManager()

    def __str__(self):
        return "%s %s (%s)" % (self.brother.first_name, self.brother.last_name, self.position)

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"

    def name(self):
        return "%s %s" % (self.brother.first_name, self.brother.last_name)

class NCCGAdvisor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.CharField(max_length=300)
    bio = models.TextField()

    class Meta:
        verbose_name = "advisor"
        verbose_name_plural = "advisors"

    def name(self):
        return "%s %s" % (self.first_name, self.last_name)

class NCCGPartner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.CharField(max_length=300)
    bio = models.TextField()
    linkedin = models.CharField(max_length=300)

    def name(self):
        return "%s %s" % (self.first_name, self.last_name)

class NCCGClient(models.Model):
    company_name = models.CharField(max_length=40)
    semester = models.CharField(max_length=100)
    description = models.TextField()

    def name(self):
        return "%s %s" % (self.first_name, self.last_name)