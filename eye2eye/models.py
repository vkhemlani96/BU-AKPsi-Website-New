from django.db import models
from buakpsi.models import PositionManager
from brothers.models import Brother
from datetime import date
import re

class Eye2EyeManager(PositionManager):
  positions = [
    "President",
    "Vice President",
    "Director of Finance",
    "Director of Research",
    "Director of Operations",
    "Director of Marketing",
    "Director of Public Relations"
  ]

class Eye2EyeMember(models.Model):
  brother = models.OneToOneField(Brother)
  position = models.CharField(max_length=45)
  bio = models.TextField()
  objects = Eye2EyeManager()

  def __str__(self):
    return "%s %s (%s)" % (self.brother.first_name, self.brother.last_name, self.position)

  class Meta:
    verbose_name = "Member"
    verbose_name_plural = "Members"

class BlogArticle(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(Brother)
  created_at = models.DateField(default=date.today)
  body = models.TextField()
  footnotes = models.TextField()
  slug = models.SlugField()

  def __str__(self):
    return "%s (by %s %s)" % (self.title, self.author.first_name, self.author.last_name)

  def preview(self):
    preview = re.sub(r"\s\s+",'', self.body) # Remove newlines
    preview = re.sub(r"<sup>\d+</sup>",'', preview) # Remove footnotes
    
    index = 0
    while index < 1000 and index < len(preview)-1:
      index += preview[index:].index("</p>") + 4

    return preview[:index]

  class Meta:
    verbose_name = "Blog Article"
    verbose_name_plural = "Blog Articles"
    ordering = ['-created_at']