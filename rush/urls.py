from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup/(?P<src>.*)$', views.signup),
    url(r'^event/(?P<name>.*)$', views.event),
    url(r'^data', views.data),

]
