# coding=utf-8
from piston.handler import BaseHandler
from access.changeUserPassword import ChangeUserPassword
from access.mail import send_generic_mail
from smtplib import *

from django.conf import settings
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
User = get_user_model()

import logging
logger = logging.getLogger('sodexologger')


class UserHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = User
    fields = ('id', 'username', 'email')

    def read(self, request, id=None, start_id=None):
        if id:
            try:
                return dict(result=User.objects.get(id=id))
            except ObjectDoesNotExist:
                return HttpResponse('Not found', status=404)
        else:
            return dict(result=User.objects.all(),
                total=User.objects.count())


class UserAuthenticationHandler(BaseHandler):
    allowed_methods = ('PUT',)
    model = User

    def update(self, request, id):
        logger.info('Starting process to change the user password')
        try:
            user = User.objects.get(id=id)
            cup = ChangeUserPassword()
            newPass = cup.aplyChange(user)
            logger.info('The new password for the user was created'
                        + ' successfully in data base.')

            send_generic_mail(settings.PASSWORD_RECOVER_EMAIL_SUBJECT,
               settings.PASSWORD_RECOVER_EMAIL_MESSAGE + newPass, [user.email])

            logger.info('The new password was sent successfully by email '\
                        + 'to user.')
            return {'result': 'Sua nova senha foi gerada com sucesso'\
                    ' e enviada por email'}
        except ObjectDoesNotExist:
                logger.warning("The user wasn't found in data base")
                return HttpResponse('Not found', status=404)
        except Exception, e:
                logger.error("Failed process to generate new password."\
                            + "ERROR: %s" % str(e))
                return HttpResponse('A new password was created but the '\
                ' Emails server is unavailable now. Please try again later.',
                    status_code=500)
