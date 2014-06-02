# coding=utf-8
from django.conf.urls import *
from piston.resource import Resource

from access import handlers

user_handler = Resource(handlers.UserHandler)
user_authentication_handler = Resource(handlers.UserAuthenticationHandler)

urlpatterns = patterns('',
    url(r'login', 'access.views.do_login'),
    url(r'logout', 'access.views.do_logout'),
    url(r'passwordrecover', 'access.views.recover_password'),
    url(r'createaccount', 'access.views.create_account'),
    url(r'^user/(?P<id>[0-9]+)$', user_handler),
    url(r'^user$', user_handler),
    url(r'^userauthentication/(?P<id>[0-9]+)$', user_authentication_handler),
)
