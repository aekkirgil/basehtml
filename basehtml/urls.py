from django.conf.urls.defaults import *
from django.conf import settings


# Uncomment the next two lines to enable the admin:

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'basehtml.home.views.index', name='index'),
	url(r'^index/$', 'basehtml.home.views.index', name='index'),
	url(r'^iletisim/$', 'basehtml.home.views.iletisim', name='iletisim'),
	url(r'^hakkimizda/$', 'basehtml.home.views.hakkimizda', name='hakkimizda'),
	url(r'^siparis/$', 'basehtml.home.views.siparis', name='siparis'),
    # url(r'^basehtml/', include('basehtml.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
)

