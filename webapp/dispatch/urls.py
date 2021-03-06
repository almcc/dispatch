from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tasking/', include('tasking.urls')),
    url(r'^bookmarks/', include('bookmarks.urls')),
    (r'^$', TemplateView.as_view(template_name='index.html')),
)
