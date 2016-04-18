import server


port = 7777

print("Creating server")
s = server.Server(port)

print("receiving file")
s.receive_file()

print("done")
