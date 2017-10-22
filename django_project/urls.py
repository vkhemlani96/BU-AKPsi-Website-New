from django.conf.urls import include, url
from django.contrib import admin
from buakpsi import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^brothers/', include('brothers.urls')),
    url(r'^faq/', views.faq),
    url(r'^contact/', views.contact),
]
