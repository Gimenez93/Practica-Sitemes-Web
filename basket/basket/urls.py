from django.conf.urls import patterns, include, url
from ibasket.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ibasket import views


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

    url(r'^users/(?P<pk>\w+)/$', views.UserDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),

    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$','django.contrib.auth.views.logout'),

    url(r'^register/$', register),

    url(r'^referees/(?P<pk>\w+)/$', views.RefereeDetail.as_view()),
    url(r'^referees/$', views.RefereeList.as_view()),

    url(r'^players/(?P<pk>\w+)/$', views.PlayerDetail.as_view()),
    url(r'^players/$', views.PlayerList.as_view()),

    url(r'^teams/(?P<pk>\w+)/$', views.TeamDetail.as_view()),
    url(r'^teams/$', views.TeamList.as_view()),

    url(r'^matches/(?P<match>\w)/(?P<idComment>\w+)/edit/$', edit),
    url(r'^matches/(?P<match>\w)/(?P<idComment>\w+)/delete/$', delete),
    url(r'^matches/(\w+)/create/$', create),
    url(r'^matches/(?P<pk>\w+)/$', views.MatchDetail.as_view()),
    url(r'^matches/$', views.MatchList.as_view()),


    url(r'^comments/(\w+)/$', comments),





)
