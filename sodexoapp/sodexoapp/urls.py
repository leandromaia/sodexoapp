from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^access/', include('access.urls')),
    url(r'^$', 'access.views.show_system'),
    url(r'^consultation/', include('consultation.urls'))
)
