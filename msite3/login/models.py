from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    password= models.CharField(max_length=200)
    friends=models.ManyToManyField("self", null=True ,blank=True, default=None)
    def __str__(self):
        return self.name

##class FriendList(models.Model):
##    name=models.ForeignKey(User)
##    friends=models.ManyToManyField(User)
##    def __str__(self):
##        return self.name
