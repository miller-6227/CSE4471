import server


port = 6000

print("Creating server")
s = server.Server(port)

print("receiving file")
s.receive_file()

print("done")
