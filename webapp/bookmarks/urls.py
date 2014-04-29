from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'bookmarks.views.index'),

    url(r'^link/$', 'bookmarks.views.newLink'),
    url(r'^link/(\d+)/$', 'bookmarks.views.viewLink'),
    url(r'^link/edit/(\d+)/$', 'bookmarks.views.editLink'),
    url(r'^link/delete/(\d+)/$', 'bookmarks.views.deleteLink'),

    url(r'^tag/$', 'bookmarks.views.newTag'),
    url(r'^tag/(\d+)/$', 'bookmarks.views.viewTag'),
    url(r'^tag/edit/(\d+)/$', 'bookmarks.views.editTag'),
    url(r'^tag/delete/(\d+)/$', 'bookmarks.views.deleteTag'),

    url(r'^tag/move/up/(\d+)/$', 'bookmarks.views.moveTagUp'),
    url(r'^tag/move/down/(\d+)/$', 'bookmarks.views.moveTagDown'),
    url(r'^tag/move/left/(\d+)/$', 'bookmarks.views.moveTagLeft'),
    url(r'^tag/move/right/(\d+)/$', 'bookmarks.views.moveTagRight'),
)
