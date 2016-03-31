CSE 4471
Daniel Miller

Summary of program:
The server program listens on a port for a connection. Once receiving a connection, it will take the recieved data to a file in a subdirectory called recv.
The client program establishes a connection with the server and then sends a copy of a file.
After copying the file, the files and connections are closed.

Running the program:
First run the server program by the following command:
python3 server.py <local-port>
Then run the client program with the following:
python3 client.py <remote-IP> <remote-port> <local-file-to-transfer>
The new file is located at recv/<filename>

