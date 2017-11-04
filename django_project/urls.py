from django.conf.urls import include, url
from django.contrib import admin
from buakpsi import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^brothers\/*', include('brothers.urls')),
    url(r'^contact/', views.contact),
    url(r'^eye2eye/', include('eye2eye.urls')),
    url(r'^faq/', views.faq),
    url(r'^nccg/', include('nccg.urls')),
    url(r'^rush\/*', include('rush.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
