from classes import receiver


# initialize a client
c = receiver.Client("", 1000)

# generate a key
c.generate_key_text()
