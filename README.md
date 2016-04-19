TODO:
(1) transfer.html template call method from view based class TransferView

    (a) sending needs the current user, friend, and file
    
    (b) receiving needs the current user

(2) correct TransferView methods send() and receive()

(3) make sure User.send_file and User.receive_file work

    (a) modify send_file to set up the file for transfer

(4) style everything





CSE 4471 - Spring 2016

Daniel Miller,
Stephen Yau,
Jimmy Kang,
Tatsumi


Summary of included program:
  server.py --> The server program listens on a port for a connection. Once receiving a connection, it will take the recieved data to a file in a subdirectory called recv.
  client.py --> The client program establishes a connection with the server and then sends a copy of a file.
  After copying the file, the files and connections are closed.
  
Database notes:
  
  Contain Database tables for users. cd into directory folder is in. Then 'cd msite'.
  login/models.py contains the users
  
  To see database tables, 'python manage.py sqlmigrate login 0002'
  To go to the admin page: 'python manage.py runserver'. User:admin Password:infosecurity
  To explore database API: 'python manage.py shell' Once you're in the shell, 'from login.models import User'
  ->'User.objects.all()' gets the users in the system
  ->'from django.utils import timezone' imports timezone so we can track when users make their accounts
  ->' "name" =User(name= "Username" ,create_date= timezone.now() , password= "password" )' creates a new user
  ->' "Username".save()' saves the user
  
