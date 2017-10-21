from django.db import models
from django.db.models import Case, When, Value, IntegerField
from brothers.models import Brother

class NCCGManager(models.Manager):
    positions = [
        'Executive Director',
        'Engagement Manager',
        'Senior Associate',
        'Associate'
    ]

    def get_queryset(self):
        return super(NCCGManager, self).get_queryset().annotate(
            position_order=Case(
                *[When(position=x, then=Value(i)) for i, x in enumerate(self.positions)],
                output_field = IntegerField()
            )
        ).order_by('position_order')

class NCCGMember(models.Model):
    # Order is done through sorting in view
    brother = models.OneToOneField(Brother)
    position = models.CharField(max_length=45)
    bio = models.TextField()
    # objects = NCCGManager()

    def __str__(self):
        return "%s %s (%s)" % (self.brother.first_name, self.brother.last_name, self.position)

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"