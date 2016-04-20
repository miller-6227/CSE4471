import sys
from classes import receiver

server_ip = sys.argv[1]
server_port = "7777"

c = receiver.Client(server_ip, server_port)

c.receive_file()
