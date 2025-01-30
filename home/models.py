# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    email = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Broker(models.Model):

    #__Broker_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    clientcode = models.CharField(max_length=255, null=True, blank=True)

    #__Broker_FIELDS__END

    class Meta:
        verbose_name        = _("Broker")
        verbose_name_plural = _("Broker")


class Telegram(models.Model):

    #__Telegram_FIELDS__
    botid = models.CharField(max_length=255, null=True, blank=True)
    token = models.CharField(max_length=255, null=True, blank=True)

    #__Telegram_FIELDS__END

    class Meta:
        verbose_name        = _("Telegram")
        verbose_name_plural = _("Telegram")



#__MODELS__END
