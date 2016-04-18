from django.db import models

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

