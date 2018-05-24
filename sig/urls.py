from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^team', views.team),
    url(r'^advisors', views.advisors),
    url(r'^partners', views.partners),
    url(r'^clients', views.clients),
]
