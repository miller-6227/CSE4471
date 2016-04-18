import sys
import os.path
import socket
import struct

from . import rsa


""" requirements:
(1) the file to be sent must in a subdirectory in called '/transfer_file'
(2) initialize a client with a remote ip and port
    i.e. c = Client(remote_ip, remote_port)
(3) send a file with c.send_file(filename) after intialization
"""
class Client:

    # initialize a client connection. need an ip and port to transfer to
    def __init__(self, remote_ip, remote_port):
        self.remote_ip, self.remote_port = remote_ip, remote_port

    # (private method) open file for reading
    def __open_file(self, filename):
        try:
            return open('./transfer_file/' + filename, 'rb')         # binary mode
        except:
            print("Unable to open the named file")
            quit()


    # method to open a connection to send a file
    def send_file(self, filename):

        # establish connection
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.remote_ip, self.remote_port))
        except:
            print("Failed to establish connection")
            quit()

        ''' get the public key needed to encrypt '''
        key = [0, 0]
        try:
            data = s.recv(512)  # received data
            key[0] = int.from_bytes(data, 'little') # bytes to int
            s.send("1".encode('utf-8')) # send ack

            data = s.recv(512)  # same thing
            key[1] = int.from_bytes(data, 'little')
            s.send("1".encode('utf-8'))          
        except:
            print("Failed to receive public key")
            quit()    

        ''' prepare the header '''
        # open the file
        local_file = self.__open_file(filename)

        # ensure that the name is exactly 20 bytes
        if (len(filename) > 20):
            filename = filename[0:20]
        elif (len(filename) < 20):
            while(len(filename) != 20):
                filename += '\0'
               
        # get the file size
        try:
            size = os.path.getsize('./transfer_file/' + "test.jpg")
        except:
            print("Unable to get the size of the local file")
            quit()
 
        ''' Send the header '''

        # send the size
        try:
            data = struct.pack("i", size)
            s.send(data)                  # send the size
        except:
            print("Failed to send file size")
            quit()

        try:
            s.send(filename.encode('utf-8'))      # send the name
        except:
            print("Failed to send file name")
            quit()

        ''' prepare and encrypt the data of the file itself '''
        # create a crypto class
        crypter = rsa.Crypto()
        a, b = key[0], key[1]

        ''' Send the encrypted file '''
        # prepare the file: get integer representation and encrypt it
        data_size = 50
        data = b''
        try:
            print("Encrypting and sending file...")
            count = 0
            while 1:
                chunk = local_file.read(data_size)
                if chunk == b'': break
                # encrypt the data
                try:
                    int_rep = int.from_bytes(chunk, 'little')       # bytes to integer
                    int_length = len(chunk)                         # byte length for reversing
                    cipher_int = crypter.encrypt(int_rep, key[0], key[1])   # encrypt integer
                    cipher = cipher_int.to_bytes(100, 'little') # integer back to bytes for transfer
                except:
                    print("Unable to encrypt the file integer representation")            
                    quit()
                # send the data
                try:
                    # first send the size of the byte string, needed to decode
                    int_length = struct.pack('i', int_length) # pack it
                    s.send(int_length)  # send it
                    s.recv(1)       # ack
                    # then send the file data (encrypted) itself
                    s.send(cipher)  # it's already bytes. so just send
                    s.recv(1)       # ack
                except:
                    print("Unable to send the cipher")
                    quit()
        except:
            print("Unable to prepare file")
            quit()
     
        # finish connection
        try:
            s.close()
        except:
            print("Failed to close connection")
        # close the file
        try:
            local_file.close()
        except:
            print("Failed to close the local file")


