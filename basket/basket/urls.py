from django.conf.urls import patterns, include, url
from ibasket.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'basket.views.home', name='home'),
    # url(r'^basket/', include('basket.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mainpage, name='home'),

    url(r'^users/(\w+)/$', userpage),
    url(r'^users/$', users),

    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$','django.contrib.auth.views.logout'),

    url(r'^register/$', register),

    url(r'^referees/(\w+)/$', referees),
    url(r'^referees/$', referee),

    url(r'^players/(\w+)/$', player),
    url(r'^players/$', players),

    url(r'^teams/(\w+)/$', team),
    url(r'^teams/$', teams),

    url(r'^matches/(\w+)/$', match),
    url(r'^matches/$', matches),


    url(r'^comments/(\w+)/$', comments),




)
