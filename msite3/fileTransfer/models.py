from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
import subprocess, os
from subprocess import PIPE, Popen
from django.contrib.auth.models import User #added this for User stuff


class UserProfile(models.Model):
    #this line is required
    user = models.OneToOneField(User)

    #More attributes?
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.user.username



class Document(models.Model):
    #user = models.OneToOneField(User)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    
    def filename(self):
        return os.path.basename(self.docfile.name)

    def path(self):
        return os.path.abspath(self.docfile.name)

