from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djcom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^catalog/?', 'views.home'),

)

urlpatterns += patterns('',
    (r'^catalog/$', 'preview.views.home'),
#    (r'^static/(?P<path>.*)$', 'django.views.static.serve,'
#{ 'document_root' : '/home/tt/.virtualenvs/project_j/djcom/static' })
)

if settings.DEBUG:
urlpatterns += patterns('',
(r'^static/(?P<path>.*)$', 'django.views.static.serve',
{ 'document_root' : '/home/tt/.virtualenvs/project_j/djcom/static' }),
)