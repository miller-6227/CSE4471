import sys
import os.path
import socket
import struct
import pickle
import rsa

""" requirements:
(1) the file to be sent must in a subdirectory in called '/transfer_file'
(2) initialize a client with a remote ip and port
    i.e. c = Client(remote_ip, remote_port)

"""
class Client:

    # initialize a client connection. need an ip and port to transfer to
    def __init__(self, remote_ip, remote_port):
        self.remote_ip, self.remote_port = remote_ip, remote_port

    # (private method) open file for reading
    def __open_file(self, filename):
        try:
            return open(filename, 'rb')         # binary mode
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
        try:
            data = s.recv(512)
            key = struct.unpack("ii", data)
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
            size = os.path.getsize('./' + "test.jpg")
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
        # send the rest of the file (sent in the TCP stream)
        data_size = 25                       # set the data size to read at a time
        try:
            count = 0
            while 1:
                chunk = local_file.read(data_size)  # read the specified size of data from the file
                if chunk == b'':
                    break
                chunk = str(chunk)
                chunk = chunk[2:len(chunk)-1]
                try:
                    chunk = crypter.encrypt(chunk, a, b) # encrypt the chunk
                except:
                    print("Error encrypting data")
                    quit()
                data_string = pickle.dumps(chunk)
                s.send(data_string)               	# send the data chunk
                s.recv(1)
                count += data_size
                print((count/size)*100, " percent")
        except:
            print("Error sending the file data")
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


