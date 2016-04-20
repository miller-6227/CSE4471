import sys
import os.path
import socket
import struct
from . import rsa

class Client:

    # initialize a client connection. need an ip and port to transfer to
    def __init__(self, remote_ip, remote_port):
        self.remote_ip, self.remote_port = remote_ip, int(remote_port)

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


        ''' get the public key '''
        # select a location
        try:
            path = os.path.dirname(os.path.realpath(__file__))
            path = os.path.join(path, os.pardir)
            path = os.path.join(path, "files")   
            key_path = os.path.join(path, "public.txt")
        except:
            print("Error selecting file path")
            quit()
        # open a the key txt file
        try:
            key_file = open(key_path, 'r')
        except:
            print("Error creating key.txt file")
            quit()
        public_key = ""
        for txt in key_file:
            public_key += txt
        public_key = public_key[1:len(public_key)-1]
        public_key = public_key.split(',')
        e, n = int(public_key[0]), int(public_key[1])

        ''' prepare the header '''
        # open the file
        local_file = self.__open_file(filename)
               
        # get the file size
        try:
            path = os.path.dirname(os.path.realpath(__file__))
            path = os.path.join(path, os.pardir)
            path = os.path.join(path + '/transfer_file/')
            print(path)
            size = os.path.getsize(path + filename)
        except:
            print("Unable to get the size of the local file")
            quit()
 
        # ensure that the name is exactly 20 bytes
        if (len(filename) > 20):
            filename = filename[0:20]
        elif (len(filename) < 20):
            while(len(filename) != 20):
                filename += '\0'

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
        ''' Send the encrypted file '''
        crypto = rsa.Crypto()
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
                    cipher_int = crypto.encrypt(int_rep, e, n)   # encrypt integer
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
            print("Unable to send and encrypt file")
            quit()
    

 
        print("done.")


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


