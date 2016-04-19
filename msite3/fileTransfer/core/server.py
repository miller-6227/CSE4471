
import os.path
import sys
import socket
import time
import struct


import rsa


'''
(1) Initialize like s = Server(local_port)
(2) receive a file like s.receive_file()
'''
class Server:
    
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
            print(HOST, self.local_port)
            s.bind((HOST, self.local_port))
            print("C")
            s.listen(1)
            print("D")
            conn, addr = s.accept()
            print("E")
            time.sleep(1)
        except:
            print("Failed to establish connection")
            quit()

        ''' generate a key and send the public key '''
        # create a crypto class for rsa 
        crypter = rsa.Crypto()
        # generate keys, using 8 bits for speed 
        print("Generating a key pair")
        a,b = crypter.generate_key(128)
        print("Generated. Now sending")

        # send the public key
        try:
            byte_len = len(str(a))          # get the length for to bytes
            data = a.to_bytes(byte_len, 'little')   # int to bytes
            conn.send(data)             # send it
            conn.recv(1)                # ack

            byte_len = len(str(a))      # same thing
            data = b.to_bytes(byte_len, 'little')
            conn.send(data)
            conn.recv(1)
            
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
        path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(path, "test")
        if not os.path.isdir(path):
            try:
                os.mkdir(path)
            except:
                print("unable to create subdirectory")
                quit()

        file_path = os.path.join(path, name)       # path to the subdirectory + /filename
        try:
            new_file = open(file_path, 'wb')                    # return a opened file
        except:
            print("Error creating file at the given path")
            quit()

        ''' get (update) the rest of the file (sent in the TCP stream) '''
        while 1:
            # recieve the size of the byte string
            try:
                data = conn.recv(512)
                if data == b'': break
                size_bytes, = struct.unpack('i', data)
                conn.send("1".encode('utf-8'))   # send the ack
            except:
                print("Failed to receive the size of the byte string")
                quit()
            # recieve the encoded cipher data
            try:
                data = conn.recv(512)
                conn.send("1".encode('utf-8'))   # send the ack
            except:
                print("Failed to receive the file contents")        
            # decrypt the data
            try:
                int_rep = int.from_bytes(data, 'little')       # get the integer rep of the cipher
                int_rep = crypter.decrypt(int_rep)             # decrypt the cipher
                data = int_rep.to_bytes(size_bytes, 'little')  # convert the decrypted cipher to bytes
            except:
                print("Failed to decrypt the data")
                quit()
            # write it to the new file            
            try:
                new_file.write(data)
            except:
                print("Unable to write the file")
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


# executing code

print("running")

# get the args
port = sys.argv[1]

# create a server
s = Server(port)

s.receive_file()

time.sleep(5)
