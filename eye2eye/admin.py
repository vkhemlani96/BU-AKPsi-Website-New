from django.contrib import admin
from eye2eye.models import Eye2EyeMember

class Eye2EyeMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_display_links = ('name',)

    def name(self, obj):
    	return "%s %s" % (obj.brother.first_name, obj.brother.last_name)


admin.site.register(Eye2EyeMember, Eye2EyeMemberAdmin)