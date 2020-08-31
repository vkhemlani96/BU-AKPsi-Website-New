from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from buakpsi import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^brothers\/*', include('brothers.urls')),
    url(r'^contact/', views.contact),
    url(r'^eye2eye/', include('eye2eye.urls')),
    url(r'^faq/', views.faq),
    url(r'^nccg/', include('nccg.urls')),
    url(r'^sfg/', include('sfg.urls')),
    url(r'^recruitment\/*', include('rush.urls')),

    url(r'^rush_resumes/(?P<path>.*)$', serve, {'document_root': 'rush_resumes'}),
    url(r'^rush_pics/(?P<path>.*)$', serve, {'document_root': 'rush_pics'}),

    url(r'^admin/', include(admin.site.urls)),
]
