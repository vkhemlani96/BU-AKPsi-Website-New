from .models import Drink
from rest_framework import serializers

class DrinkSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Drink
		fields = ('name','brew_type','brew_temp','brew_pressure','brew_time')