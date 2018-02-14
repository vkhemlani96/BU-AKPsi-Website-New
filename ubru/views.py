from django.http import HttpResponse

from rest_framework import viewsets, permissions, renderers, status
from rest_framework.response import Response

from .models import User, UUID, Drink
from .serializers import DrinkSerializer

class DrinksViewSet(viewsets.ModelViewSet):

    queryset = Drink.objects.all()

    serializer_class = DrinkSerializer
    permission_classes = (permissions.AllowAny,)

    def list(self, request, uuid): # pylint: disable=unused-argument

        drinks = UUID.objects.get(identifier=uuid).user.drinks

        return Response(self.get_serializer(instance=drinks, many=True).data)

    def create(self, request):

      data = request.data
      uuid = int(data["uuid"])

      drink_data = {
        "name": data["name"],
        "brew_type": data["type"],
        "brew_temp": int(data["temp"]),
        "brew_pressure": int(data["pressure"]),
        "brew_time": int(data["time"])
      }

      drink = Drink(**drink_data)
      drink.save()
      UUID.objects.get(identifier=uuid).user.drinks.add(drink)

      return Response(None, status=status.HTTP_201_CREATED)