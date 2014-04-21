from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'location.views.index'),
 
    url(r'^link/$', 'location.views.newLink'),
    url(r'^link/(\d+)/$', 'location.views.editLink'),
    url(r'^link/delete/(\d+)/$', 'location.views.deleteLink'),
 
    url(r'^tag/$', 'location.views.newTag'),
    url(r'^tag/(\d+)/$', 'location.views.editTag'),
    url(r'^tag/delete/(\d+)/$', 'location.views.deleteTag'),

    url(r'^tag/move/up/(\d+)/$', 'location.views.moveTagUp'),
    url(r'^tag/move/down/(\d+)/$', 'location.views.moveTagDown'),
    url(r'^tag/move/left/(\d+)/$', 'location.views.moveTagLeft'),
    url(r'^tag/move/right/(\d+)/$', 'location.views.moveTagRight'),
)
