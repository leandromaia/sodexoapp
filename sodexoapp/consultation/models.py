# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models


class SodexoClient(models.Model):

    user = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    card_number = models.CharField(max_length=30)
    daily_value = models.DecimalField(max_digits=6, decimal_places=2,
                                                                default=00.00)

    def __unicode__(self):
        return self.name
