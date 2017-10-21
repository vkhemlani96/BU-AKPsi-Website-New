from django.db import models

class PositionManager(models.Manager):
    def get_queryset(self):
        return super(type(self), self).get_queryset().annotate(
            position_order=Case(
                *[When(position=x, then=Value(i)) for i, x in enumerate(self.positions)],
                output_field = IntegerField()
            )
        ).order_by('position_order', 'brother__last_name')