import sys
import os.path
import socket
import struct
from . import rsa



class Client:

    # initialize a client connection. need an ip and port to transfer to
    def __init__(self, remote_ip, remote_port):
        self.remote_ip, self.remote_port = remote_ip, int(remote_port)

    # generate key and prepare key.txt
    def generate_key_text(self):
        try:
            print("Generating key...")
            crypter = rsa.Crypto()
            private_key, public_key = crypter.generate_key(128)
            print("Key generated.")
        except:
            print("Error generating RSA keys")
            quit()

        # prepare the text file to be send
        # select a location
        try:
            path = os.path.dirname(os.path.realpath(__file__))
            path = os.path.join(path, os.pardir)
            path = os.path.join(path, "files")
            public_key_path = os.path.join(path, "public.txt")
            private_key_path = os.path.join(path, "private.txt")
        except:
            print("Error selecting file path")
            quit()
        # open a the key txt file
        try:
            private_file = open(private_key_path, 'w')
            public_file = open(public_key_path, 'w')
        except:
            print("Error creating key.txt file")
            quit()
        # fill the file
        try:
            private_file.write(str(private_key)) 
            public_file.write(str(public_key)) 
        except:
            print("Failed to write to the key file")
            quit()
        # close the file
        try:
            private_file.close()
            public_file.close()
        except:
            print("Failed to close the file")
            quit()

    def receive_file(self):
        # establish connection:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.remote_ip, self.remote_port))
        except:
            print("Failed to establish connection")
            quit()
      
        ''' receive the header '''
        # get first 4 bytes (contains the number of bytes in the file to follow)	
        try:
            data = s.recv(4)
            size, = struct.unpack("i", data)
        except:
            print("Failed to receive size")
            quit()
        print("Filesize: ", size)

        # get next 20 bytes (contains the name of the file)
        try:
            name = s.recv(20)    # get the 20 byte name
            name = name.decode('utf-8')
            name = name.strip('\0')
        except:
            print("Failed to receive filename")
            quit()
        print("Filename: ", name)

        ''' select where to save the received file ''' 
        path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(path, os.pardir)
        path = os.path.join(path, "files")
        file_path = os.path.join(path, name)       # path to the subdirectory + /filename
        try:
            new_file = open(file_path, 'wb')                    # return a opened file
        except:
            print("Error creating file at the given path")
            quit()

        ''' get the private key '''
         # select a location
        try:
            path = os.path.dirname(os.path.realpath(__file__))
            path = os.path.join(path, os.pardir)
            path = os.path.join(path, "files")
            private_key_path = os.path.join(path, "private.txt")
        except:
            print("Error selecting file path")
            quit()
        # open a the key txt file
        try:
            private_file = open(private_key_path, 'r')
        except:
            print("Error creating key.txt file")
            quit()
        private_key = ""
        for txt in private_file:
            private_key += txt

        private_key = private_key[1:len(private_key)-1]
        private_key = private_key.split(',')

        d = int(private_key[0])
        n = int(private_key[1])
            
        ''' get (update) the rest of the file (sent in the TCP stream) '''
        crypter = rsa.Crypto()
        while 1:
            # recieve the size of the byte string
            try:
                data = s.recv(512)
                if data == b'': break
                size_bytes, = struct.unpack('i', data)
                s.send("1".encode('utf-8'))   # send the ack
            except:
                print("Failed to receive the size of the byte string")
                quit()
            # recieve the encoded cipher data
            try:
                data = s.recv(512)
                s.send("1".encode('utf-8'))   # send the ack
            except:
                print("Failed to receive the file contents")        
            # decrypt the data
            try:
                int_rep = int.from_bytes(data, 'little')       # get the integer rep of the cipher
                int_rep = crypter.decrypt(int_rep, d, n)             # decrypt the cipher
                data = int_rep.to_bytes(int(size_bytes), 'little')  # convert the decrypted cipher to bytes
            except:
                print("Failed to decrypt the data")
                quit()
            # write it to the new file            
            try:
                new_file.write(data)
            except:
                print("Unable to write the file")
                quit()
 
        
        # finish connection
        try:
            s.close()
        except:
            print("Failed to close connection")
        # close the file
        try:
            private_file.close()
            new_file.close()
        except:
            print("Failed to close the local file")


