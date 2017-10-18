from django.contrib import admin
from .models import Brother, EBoardMember

class EBoardMemberAdmin(admin.ModelAdmin):
    list_display = ('order', 'position', 'brother')
    list_display_links = ('order', 'position')
    ordering = ['order']

admin.site.register(Brother)
admin.site.register(EBoardMember, EBoardMemberAdmin)
