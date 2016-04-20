import sys
from classes import sender


server_ip = sys.argv[1]
server_port = "6667"
filename = str(sys.argv[2])

c = sender.Client(server_ip, server_port)

c.send_file(filename)
