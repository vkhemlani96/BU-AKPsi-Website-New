from django.contrib import admin
from sfg.models import SFGMember

class SFGMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_display_links = ('name',)
    list_filter = ('position',)

