from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'location.views.index'),
    url(r'^link/$', 'location.views.newLink'),
    url(r'^link/(\d+)/$', 'location.views.editLink'),
    url(r'^link/delete/(\d+)/$', 'location.views.deleteLink'),
)
