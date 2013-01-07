from django.conf.urls import patterns, include, url
from app1.views import hello_view,home_view,buttons_view, tabs_view

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'megatemplate.views.home', name='home'),
    # url(r'^megatemplate/', include('megatemplate.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', view=hello_view, name='hello_page'),
    url(r'^buttons/', view=buttons_view, name='buttons_page'),
    url(r'^tabs/', view=tabs_view, name='tabs_page'),
    url(r'^$', view=home_view, name='home_page'),
)
