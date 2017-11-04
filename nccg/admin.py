from django.contrib import admin
from nccg.models import NCCGMember, NCCGAdvisor, NCCGPartner, NCCGClient

class NCCGMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_display_links = ('name',)
    list_filter = ('position',)

class NCCGAdvisorAdmin(admin.ModelAdmin):
	list_display = ('name', 'title')
	list_display_links = ('name',)

class NCCGPartnerAdmin(admin.ModelAdmin):
	list_display = ('name', 'title')
	list_display_links = ('name',)

class NCCGClientAdmin(admin.ModelAdmin):
	list_display = ('company_name',)
	list_display_links = ('company_name',)


admin.site.register(NCCGMember, NCCGMemberAdmin)
admin.site.register(NCCGAdvisor, NCCGAdvisorAdmin)
admin.site.register(NCCGPartner, NCCGPartnerAdmin)
admin.site.register(NCCGClient, NCCGClientAdmin)