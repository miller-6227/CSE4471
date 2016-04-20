
**Secure File Transfer**

CSE 4471 - Spring 2016

Daniel Miller
Stephen Yau
Jimmy Kang
Tatsumi Suenaga

**Description**

A file transfer web application built using Django with RSA file encryption that allows users to securely send encrypted files to each other

**How to Run**

Clone project from Github: https://github.com/miller-6227/CSE4471

Go to file directory:

    cd CSE4471
    cd msite3
Migrate the database

    python manage.py makemigrations
    python manage.py migrate
Run web app on local server

    python manage.py runsslserver

Open the development server link 

    https://127.0.0.1:8000/


**Summary of included files:**

  server.py --> The server program listens on a port for a connection. Once receiving a connection, it will take the recieved data to a file in a subdirectory called recv.
  client.py --> The client program establishes a connection with the server and then sends a copy of a file.
  After copying the file, the files and connections are closed.
  
**Database Notes:**
  
  Contain Database tables for users. cd into directory folder is in. Then 'cd msite'.
  login/models.py contains the users
  
  To see database tables, 'python manage.py sqlmigrate login 0002'
  To go to the admin page: 'python manage.py runserver'. User:admin Password:infosecurity
  To explore database API: 'python manage.py shell' Once you're in the shell, 'from login.models import User'
  ->'User.objects.all()' gets the users in the system
  ->'from django.utils import timezone' imports timezone so we can track when users make their accounts
  ->' "name" =User(name= "Username" ,create_date= timezone.now() , password= "password" )' creates a new user
  ->' "Username".save()' saves the user
  

