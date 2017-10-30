from django.contrib import admin
from eye2eye.models import Eye2EyeMember, BlogArticle

class Eye2EyeMemberAdmin(admin.ModelAdmin):
  list_display = ('name', 'position')
  list_display_links = ('name',)

  def name(self, obj):
    return "%s %s" % (obj.brother.first_name, obj.brother.last_name)

class BlogArticleAdmin(admin.ModelAdmin):
  list_display = ('title', 'author_name', 'created_at')
  list_display_links = ('title',)

  prepopulated_fields = {"slug": ("title",)}

  def author_name(self, obj):
    return "%s %s" % (obj.author.first_name, obj.author.last_name)
  

admin.site.register(Eye2EyeMember, Eye2EyeMemberAdmin)
admin.site.register(BlogArticle, BlogArticleAdmin)