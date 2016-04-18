
import os.path
import sys
import socket
import time
import struct

import rsa

class Server(rsa.Crypto):
    
    # initialize a server connection class
    def __init__(self, local_port):
        self.local_port = local_port 

    # receive the file on a local port
    def receive_file(self):
        ''' set up the connection '''
        HOST = ''
        # establish connection
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((HOST, self.local_port))
            s.listen(1)
            conn, addr = s.accept()
            time.sleep(1)
        except:
            print("Failed to establish connection")
            quit()

        ''' generate a key and send the public key '''
        # create a crypto class for rsa 
        crypter = Crypto()
        # generate keys, using 8 bits for speed 
        key = crypter.generate_key(8)
        # send the public key
        try:
            data = struct.pack("i", key)
            s.send(data)
        except:
            print("Unable to send the public key")
            quit()

        ''' receive the header '''
        # get first 4 bytes (contains the number of bytes in the file to follow)	
        try:
            data = conn.recv(4)
            size, = struct.unpack("i", data)
        except:
            print("Failed to receive size")
            quit()
        print("Filesize: ", size)

        # get next 20 bytes (contains the name of the file)
        try:
            name = conn.recv(20)    # get the 20 byte name
            name = name.decode('utf-8')
            name = name.strip('\0')
        except:
            print("Failed to receive filename")
            quit()
        print("Filename: ", name)

        ''' select where to save the received file ''' 
        path = ""
        file_path = os.path.join(path, name)       # path to the subdirectory + /filename
        try:
            return open(file_path, 'wb')                    # return a opened file
        except:
            print("Error creating file at the given path")
            quit()

        ''' get (update) the rest of the file (sent in the TCP stream) '''
        try:
            while 1:
                data = conn.recv(512)        # get the chunk of data
                if not data: break           # check for null
                data = crypter.decrypt(data) # decrypt the data
                new_file.write(data)         # write that data to the file
        except:
            print("Error receiving file contents")
            quit()



        # close the connection
        try:
            conn.close()
        except:
            print("Failed to close the connection")

        # close the files
        try:
            new_file.close()
        except:
            print("Error closing file")



