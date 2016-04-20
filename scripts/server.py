#!/usr/bin/env python

import sys
import os
import socket
import struct
import select

MSS = 1024
server_connect_port = 7777
client_connect_port = 6667

print("IP:", socket.gethostbyname(socket.gethostname()))


#######create and open port for server to connect to#######
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
        server_socket.bind((socket.gethostbyname(socket.gethostname()), server_connect_port))
        server_socket.listen(1)
except:
        print("Error connecting to the server")
        server_socket.close()
        quit()
#accepting client connection : blocking
print("listening on port "+str(server_connect_port)+" for a connection from server");

server_socket, addr = server_socket.accept()
#if here is reached, the server has connected


#######create and open port for client to connect to#######
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	client_socket.bind((socket.gethostname(),client_connect_port))
	client_socket.listen(1)
except:
        print("Error connecting to the client")
        server_socket.close()
        client_socket.close()
        quit()
#accepting client connection : blocking
print("listening on port "+str(client_connect_port)+" for a connection from client");
client_socket, addr = client_socket.accept()


######now both server and client are connected. send file between the two########
while 1:
	#waiting for data from remote-host
	inputs = [server_socket,client_socket]
	outputs = []
	#waiting for data from local-host
	readable,writeable,special = select.select(inputs,outputs,inputs)
	#determine which sockets have data ready
	for s in readable:
		if s is server_socket:
                        data = server_socket.recv(MSS)
                        if data == b'': quit()
                        client_socket.send(data)
		elif s is client_socket:
                        data = client_socket.recv(MSS)
                        if data == b'': quit()
                        server_socket.send(data)
