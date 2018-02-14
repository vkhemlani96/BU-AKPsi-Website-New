from django.contrib import admin
from .models import User, UUID, Drink

class UserAdmin(admin.ModelAdmin):
  list_display = ('name', 'phone_number')
  list_display_links = ('name',)

class UUIDAdmin(admin.ModelAdmin):
  list_display = ('identifier', )
  list_display_links = ('identifier',)

class DrinkAdmin(admin.ModelAdmin):
  list_display = ('name', )
  list_display_links = ('name',)

admin.site.register(User, UserAdmin)
admin.site.register(UUID, UUIDAdmin)
admin.site.register(Drink, DrinkAdmin)