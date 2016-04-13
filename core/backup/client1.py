import sys
import os.path
import socket
import struct

# open file for reading
def open_file(filename):
    try:
        return open(filename, 'rb')         # binary mode
    except:
        print("Unable to open the named file")
        quit()


# main program

# check correct number of command line arguments
if len(sys.argv) != 4:
    print("You need exactly 4 command line arguments")
    quit()

# get the command line arguments 
remote_ip = str(sys.argv[1])			# <remote-IP-on-gamma>
remote_port = int(sys.argv[2])		       	# <remote-port-on-gamma>
local_file = open_file(sys.argv[3])		# open <local-file-to-transfer>

# get the file information
try:
    size = os.path.getsize('./' + str(sys.argv[3]))
except:
    print("Unable to get the size of the local file")
    quit()    

# establish connection
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((remote_ip, remote_port))
except:
    print("Failed to establish connection")
    quit()

# send the size
try:
    data = struct.pack("i", size)
    s.send(data)                  # send the size
except:
    print("Failed to send file size")
    quit()

# send the name of the file
# ensure that the name is exactly 20 bytes
name = str(sys.argv[3])
if (len(name) > 20):
    name = name[0:20]
elif (len(name) < 20):
    while(len(name) != 20):
        name += '\0'
try:
    s.send(name.encode('utf-8'))      # send the name
except:
    print("Failed to send file name")
    quit()

# send the rest of the file (sent in the TCP stream)
data_size = 512                         # set the data size to read at a time
try:
    while 1:
        chunk = local_file.read(data_size)       # read the specified size of data from the file
        if not chunk:
            break;
        s.send(chunk)               		 # send the data chunk
except:
    print("Error sending the file data")
    quit()

# finish connection
try:
    s.close()
except:
    print("Failed to close connection")

# close the files
try:
    local_file.close()
except:
    print("Error closing file")




