from django.db import models

class Drink(models.Model):
  ESPRESSO = "ES"
  AMERICANO = "AM"

  name = models.CharField(max_length = 30)
  brew_type = models.CharField(
        max_length=2, choices=((ESPRESSO, "Espresso"), (AMERICANO, "Americano")))
  brew_temp = models.IntegerField()
  brew_pressure = models.IntegerField()
  brew_time = models.IntegerField()

class PastDrink(models.Model):
  drink = models.ManyToManyField(Drink)
  time = models.DateTimeField(auto_now_add=True)

class User(models.Model):
  name = models.CharField(max_length=30)
  phone_number = models.CharField(max_length=10)
  drinks = models.ManyToManyField(Drink)

class UUID(models.Model):
  identifier = models.IntegerField()
  user = models.ForeignKey(User)