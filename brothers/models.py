from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible  # only if you need to support Python 2
class Brother(models.Model):
    ACTIVE = "AC"
    INACTIVE = "IA"
    ALUMNI = "AL"
    LOA = "LO"

    email = models.CharField(max_length=8, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    class_name = models.CharField(max_length=8)
    year = models.CharField(max_length=4)
    major_school = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    minor_school = models.CharField(max_length=255)
    minor = models.CharField(max_length=255)
    linkedin = models.URLField(max_length=300)
    status = models.CharField(
        max_length=2, choices=((ACTIVE, "Active"), (INACTIVE, "Inactive"), (ALUMNI, "Alumni"), (LOA, "LOA")))
    eye2eye = models.BooleanField(default=False)
    nccg = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name
