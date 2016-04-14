import client

HOST = ''
port = 6000

print("creating client")
c = client.Client(HOST, port)


filename = "test.jpg"


print("sending file")
c.send_file(filename)

print("done")
