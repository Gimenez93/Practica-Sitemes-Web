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

    url(r'^users/(?P<pk>\w+)/$', UserDetail.as_view()),
    url(r'^users/$', UserList.as_view()),

    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$','django.contrib.auth.views.logout'),

    url(r'^register/$', register),

    url(r'^referees/(?P<pk>\w+)/$', RefereeDetail.as_view()),
    url(r'^referees/$', RefereeList.as_view()),

    url(r'^players/(?P<pk>\w+)/$', PlayerDetail.as_view()),
    url(r'^players/$', PlayerList.as_view()),

    url(r'^teams/(?P<pk>\w+)/$', TeamDetail.as_view()),
    url(r'^teams/$', TeamList.as_view()),

    url(r'^matches/(?P<match>\w+)/(?P<pk>\w+)/edit/$', UpdateComment.as_view()),
    url(r'^matches/(?P<match>\w+)/(?P<pk>\w+)/delete/$', DeleteComment.as_view()),
    url(r'^matches/(?P<pk>\d)/create/$', CreateComment.as_view()),
    url(r'^matches/(?P<pk>\w+)/$', MatchDetail.as_view()),
    url(r'^matches/$', MatchList.as_view()),


    #url(r'^comments/(\w+)/$', CommentList.as_view()),





)
