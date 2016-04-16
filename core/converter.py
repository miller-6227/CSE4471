


local_file = open("test.jpg", 'r')
new_file = open("./test/new.jpg", "wb")


while 1:
    l = local_file.read(500)
    if l == '': break
    print(l)
    new_file.write(l)
