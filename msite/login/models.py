from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


class User(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField('date made')
    password= models.CharField(max_length=200)
    def __str__(self):
        return self.name
