from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


class User(models.Model):
    name = models.CharField(max_length=200, unique=True)
    password= models.CharField(max_length=200)
    ip_address=models.CharField(max_length=200, default='127.0.0.1')
    port_number=models.CharField(max_length=10, default='6000')
    file_directory=models.CharField(max_length=1000, default='/Users/Username/Desktop ')
    friends=models.ManyToManyField("self" ,blank=True, default=None)

    def __str__(self):
        return self.name

    def send_file(self, friend, transfer_file):
        # set up the transfer file TODO
        # call the script
        subprocess.call(["python3 client.py", friend.ip_address, friend.port_number, transfer_file], shell=True)
    
    def receive_file(self):
        subprocess.call(["python3 server.py", self.port_number], shell=True)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
