# encoding: utf-8
from piston.handler import BaseHandler

from django.db import transaction
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()

from access.mail import send_generic_mail
from consultation.models import SodexoClient


class SodexoClientHandler(BaseHandler):
    allow_methods = ('GET', 'POST')
    model = SodexoClient

    fields = ('id', 'name', 'cpf', 'card_number', 'daily_value',
              ('user', ('id', 'username', 'email')))

    def read(self, request, id=None, start_id=None):
        try:
            return dict(result=SodexoClient.objects.all(),
                        total=SodexoClient.objects.count())
        except ObjectDoesNotExist:
            return {"error 404": "not found"}

    @transaction.commit_on_success
    def create(self, request, *args, **kwargs):
        if not self.has_model():
            return HttpResponse(400, "The SodexoClient model is required.")

        try:
            attrs = request.data
            user_data = attrs['user']
            user = User()
            user.username = user_data['username']
            user.set_password(user_data['password'])
            user.email = user_data['email']
            user.save()

            sodexo_client = SodexoClient()
            sodexo_client.user = user
            sodexo_client.name = attrs['name']
            sodexo_client.cpf = attrs['cpf']
            sodexo_client.card_number = attrs['card_number']
            sodexo_client.daily_value = attrs['daily_value']
            sodexo_client.save()

            send_generic_mail(settings.SODEXOCLIENT_CREATED_EMAIL_SUBJECT,\
               settings.SODEXOCLIENT_CREATED_MESSAGE + user.username,\
               [user.email])

            return {'result': sodexo_client}
        except Exception, e:
            resp = HttpResponse()
            resp.status_code = 500
            resp.write(str(e))
            return resp
