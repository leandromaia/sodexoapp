from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^access/', include('access.urls')),
    url(r'^$', 'access.views.show_system'),
    url(r'^consultation/', include('consultation.urls'))
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$',\
        'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )