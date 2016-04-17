
import random
import itertools
import fractions

class Crypto:

    # private variables as keys
    __n = 0
    __e = 0
    __d = 0

    def decrypt(self, cipher):
        #return ((cipher ** self.__d) % self.__n)
        return pow(cipher, self.__d, self.__n)

    def encrypt(self, message, e, n):
        return pow(message, e, n)
        #return ((message ** e) % n)

    def __extended_gcd(self, a, b):
        x, lastx, y, lasty, = 0, 1, 1, 0
        while b != 0:
            q, r = divmod(a, b)
            a, b = b, r
            x, lastx = lastx - q * x, x
            y, lasty = lasty - q * y, y
        return lastx, lasty


    def generate_key(self, bits):
        # find two prime number, p and q
        p = self.__get_primes(bits >> 1)
        q = self.__get_primes(bits >> 1)
        # it's very unlikely that p==q, but if they are, try again
        while (q==p):
            q = self.__get_primes(bits >> 1)

        # compute n = pq
        n = p * q
        phi = (p-1) * (q-1)

        # given a, n, and e, with 0 < a < n and e > 1, calculate a^e mod n
        while True:
            e = random.randint(3, phi - 1)
            if fractions.gcd(e, phi) == 1:
                break
        d = self.__multiplicative_inverse(e, phi)

        print(e, d, n)

        self.__n = n
        self.__e = e
        self.__d = d
        return (e, n)

    def __get_primes(self, bits):
        # get a randome number in the range of 2^(bit-1) +1 [specifies odd number] to 2^(bit) - 1
        # jump by 2s too only look at odd numbers
        p = random.randrange((2**(bits-1))+1, (2**bits)-1, 2)
        # just brute force randomly until you get a prime number
        while not self.__is_prime(p):
            if (p+2)>=(bits-1) or p%2==0:
                p = random.randrange((2**(bits-1))+1, (2**bits)-1, 2)
            else:
                p += 2
        return p

    def __is_prime(self, n):
        if n == 2 or n == 3: return True
        if n < 2 or n % 2 == 0: return False
        if n < 9: return True
        if n % 3 == 0: return False
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n % f == 0: return False
            if n % (f + 2) == 0: return False
            f += 6
        return True



    def __multiplicative_inverse(self, e, n):
        x, y = self.__extended_gcd(e, n)
        if x < 0:
            return n + x
        return x

#### test

message = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00C\x00'
print(message)
x = len(message)

integer = int.from_bytes(message, 'little')
print(integer)
length = (len(str(integer)))
print(length)


crypto = Crypto()
a,b = crypto.generate_key(length)
print(a,b)

cipher = crypto.encrypt(integer, a,b)
print(cipher)

dmessage = crypto.decrypt(cipher)
print(dmessage)
print(len(str(dmessage)))

print(dmessage.to_bytes(x, 'little'))


