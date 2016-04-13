
import os.path
import sys
import socket
import time
import struct


# create subdirectory and return the path to it
def create_subdir(subdir):
    path = os.path.dirname(os.path.realpath(__file__))  # get current path
    path = os.path.join(path, subdir)                   # join the subdir name to the path
    if not os.path.isdir(path):                         # if the path doesnt yet exist
        try:
            os.mkdir(path)                              # create the subdirectory
        except:
            print("Unable to create subdirectory")
            quit()
    return path                                         # return the path to the subdirectory

# create new (empty) file in that subdirectory
def create_new_file(path, filename):
    file_path = os.path.join(path, filename)            # path to the subdirectory + /filename
    try:
        return open(file_path, 'wb')                    # return a opened file
    except:
        print("Error creating file at the given path")
        quit()

# main program

# check command line argument count
if len(sys.argv) != 2:
    print("You need exactly 2 command line arguments")
    quit()

# get the command line arguments
HOST = ''                                       # symbolic name meaning all available interfaces
try:
    local_port = int(sys.argv[1])			# <local-port-on-gamma>
except:
    print("Error in command line arguments")
    quit()

# establish connection
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, local_port))
    print("Listening on port", str(local_port), "...")
    s.listen(1)
    conn, addr = s.accept()
    time.sleep(1)
    print('Connected by', addr)
except:
    print("Failed to establish connection")
    quit()

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

# create file
path = create_subdir("recv")                    # create subdir "recv"
new_file = create_new_file(path, name)	# create a new empty file at the path

# get (update) the rest of the file (sent in the TCP stream)
try:
    while 1:
        data = conn.recv(512)       # get the chunk of data
        new_file.write(data)        # write that data to the file
        if not data: break          # check for null
        #conn.send(data)          # send confirmation
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



