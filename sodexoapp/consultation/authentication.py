# coding: utf-8
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.core.serializers.json import DateTimeAwareJSONEncoder
from django.http import HttpResponse
from django.utils import simplejson


class DjangoAuthentication(object):
    """
    Django authentication for piston
    """
    request = None
    errors = None

    def is_authenticated(self, request):
        """
        if user is_authenticated: return True
        else try to autenticate with django and return true/false dependent of
        result
        """
        self.request = request

        # is authenticated
        if self.request.user.is_authenticated():
            return True

        # not authenticated, call authentication form
        f = AuthenticationForm(data={
            'username': self.request.POST.get('username', ''),
            'password': self.request.POST.get('password', ''),
        })

        # if authenticated log the user in.
        if f.is_valid():

            auth_login(self.request, f.get_user())
            # this ** should ** return true
            return self.request.user.is_authenticated()

        else:
            # fail to auth, save form errors
            self.errors = f.errors
            return False

    def challenge(self, request=None):
        """
        `challenge`: In cases where `is_authenticated` returns
        False, the result of this method will be returned.
        This will usually be a `HttpResponse` object with
        some kind of challenge headers and 401 code on it.
        """
        resp = {'error': 'Authentication needed', 'msgs': self.errors}
        return HttpResponse(simplejson.dumps(
                resp, cls=DateTimeAwareJSONEncoder,
                ensure_ascii=False, indent=4),
            status=401, mimetype="application/json")
