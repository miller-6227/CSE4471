import client

HOST = '128.146.165.254'
port = 7777

print("creating client")
c = client.Client(HOST, port)


filename = "test.jpg"


print("sending file")
c.send_file(filename)

print("done")
