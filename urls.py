from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from DJ_Learning.views import helloworld,current_datetime
from C1.views import dbview,category_list

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^hello/$', helloworld),
    (r'^time/plus/(\d{1,2})/$',current_datetime),
    (r'^dbview/$',dbview),
    (r'^clist/$',category_list),
    # Examples:
    # url(r'^$', 'DJ_Learning.views.home', name='home'),
    # url(r'^DJ_Learning/', include('DJ_Learning.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()