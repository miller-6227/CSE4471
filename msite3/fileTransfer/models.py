from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
import subprocess, os
from subprocess import PIPE, Popen
from django.contrib.auth.models import User #added this for User stuff

# class User(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     password= models.CharField(max_length=200)
#     ip_address=models.CharField(max_length=200, default='127.0.0.1')
#     file_directory=models.CharField(max_length=1000, default='/Users/Username/Desktop ')
#     friends=models.ManyToManyField("self" ,blank=True, default=None)

#     #def get_ip(self):

#     def __str__(self):
#         return self.name

#     def send_file(self, friend, transfer_file):
#         # set up the transfer file
#         filename = transfer_file.filename()
#         path = transfer_file.path()

#         # get the path for the client
#         dire = os.path.dirname(os.path.realpath(__file__))
#         dire = os.path.join(dire, 'core/client.py') 

#         port = '6666'

#         # call the script
#         subprocess.call(['python3', dire, friend.ip_address, str(port), path, filename])
    
#     def receive_file(self):

#         # get the path for the client
#         dire = os.path.dirname(os.path.realpath(__file__))
#         dire = os.path.join(dire, 'core/server.py') 
#         port = '6666'
#         subprocess.call(['python3', dire, str(port)])


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

