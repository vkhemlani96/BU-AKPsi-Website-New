from django.contrib import admin
from buakpsi.models import FAQ

class FAQAdmin(admin.ModelAdmin):
	list_display = ('question', )
	list_display_links = ('question',)

admin.site.register(FAQ, FAQAdmin)