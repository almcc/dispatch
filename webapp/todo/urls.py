from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'todo.views.index'),
    url(r'^task/$', 'todo.views.newTask'),
    url(r'^task/(\d+)/$', 'todo.views.editTask'),
    url(r'^task/delete/(\d+)/$', 'todo.views.deleteTask'),
)
