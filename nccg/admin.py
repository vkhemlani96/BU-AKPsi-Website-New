from django.contrib import admin
from nccg.models import NCCGMember

class NCCGMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_display_links = ('name',)
    list_filter = ('position',)

    def name(self, obj):
    	return "%s %s" % (obj.brother.first_name, obj.brother.last_name)


admin.site.register(NCCGMember, NCCGMemberAdmin)