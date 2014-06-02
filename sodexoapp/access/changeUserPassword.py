# coding=utf-8
import string
import random


class ChangeUserPassword(object):

    def aplyChange(self, user):
        newPass = ''.join([random.choice(string.ascii_letters + string.digits)
                                                        for n in xrange(8)])
        user.set_password(newPass)
        user.save()
        return newPass
