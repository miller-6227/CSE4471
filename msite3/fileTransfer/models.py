from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


class User(models.Model):
    name = models.CharField(max_length=200, unique=True)
    password= models.CharField(max_length=200)
    ip_address=models.CharField(max_length=200, default='11')
    port_number=models.CharField(max_length=10, default='6000')
    file_directory=models.CharField(max_length=1000, default='/Users/Username/Desktop ')
    friends=models.ManyToManyField("self" ,blank=True, default=None)
    def __str__(self):
        return self.name
# path to the classes, Server and Client
from .core import server
from .core import client

# class for transfering files. Both sending and recieving
class Transfer(models.Model):
    ip = ''                             # local host for testing (IP of the server)
    port = 6000                         # static for testing, MUST be the same for server/client
    receiver = server.Server(port)
    sender = client.Client(ip, port)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
