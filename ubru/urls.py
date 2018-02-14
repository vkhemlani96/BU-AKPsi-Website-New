from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DrinksViewSet

Drinks = DrinksViewSet.as_view({
  'get': 'list',
  'post': 'create',
})

urlpatterns = format_suffix_patterns([
    url (r'^drinks/uuid/(?P<uuid>[0-9]+)', Drinks),
    url (r'^drinks/', Drinks),
])
