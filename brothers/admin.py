from django.contrib import admin
from .models import Brother, EBoardMember

class BrotherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'class_name', 'status', 'year')
    list_display_links = ('first_name', 'last_name')
    ordering = ['status', 'last_name']
    list_filter = ('status', 'class_name', 'year')

class EBoardMemberAdmin(admin.ModelAdmin):
    list_display = ('order', 'position', 'brother')
    list_display_links = ('order', 'position')
    ordering = ['order']

admin.site.register(Brother, BrotherAdmin)
admin.site.register(EBoardMember, EBoardMemberAdmin)
