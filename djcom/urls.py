from djcom import settings
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls.defaults import *
from django.conf.urls import patterns, url, include
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^ecomstore/', include('ecomstore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
		#(r'^', include('catalog.urls')),
		#(r'^cart/', include('cart.urls')),
	(r'^catalog/$', 'preview.views.home'),
)

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()

handler404 = 'djcom.views.file_not_found_404'
		
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
