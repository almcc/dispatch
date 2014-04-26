from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'tasking.views.index'),
    url(r'^task/$', 'tasking.views.newTask'),
    url(r'^task/(\d+)/$', 'tasking.views.editTask'),
    url(r'^task/delete/(\d+)/$', 'tasking.views.deleteTask'),
)
