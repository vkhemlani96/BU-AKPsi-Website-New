from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^board$', views.board),
    url(r'^blog\/*$', views.blog),
    url(r'^blog/(?P<slug>.*)$', views.article),
]
