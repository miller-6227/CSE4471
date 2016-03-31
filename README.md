CSE 4471 - Spring 2016

Daniel Miller
Stephen Yau
Jimmy Kang
Tatsumi 

To do:
- Create basic Django
- view
  - front-end design
  - page for user login/creation.edit
  - list of friends
- controller
  - add exisiting python files
  - improve encryption
  - share IP and port
- database 
  - users, associated with a friend list

Summary of included program:
server.py --> The server program listens on a port for a connection. Once receiving a connection, it will take the recieved data to a file in a subdirectory called recv.
client.oy --> The client program establishes a connection with the server and then sends a copy of a file.
After copying the file, the files and connections are closed.

Running the program:
First run the server program by the following command:
python3 server.py <local-port>
Then run the client program with the following:
python3 client.py <remote-IP> <remote-port> <local-file-to-transfer>
The new file is located at recv/<filename>
