from django.core.mail import send_mail
from smtplib import *
from django.conf import settings


def send_generic_mail(subject, message, to):

    for recipient in to:
        if recipient == '':
            raise ValueError('Recipiente address invalid')

    return send_mail(subject, message, settings.SENDMAIL_FROM_ADDRESS, to,
                                                         fail_silently=False)
