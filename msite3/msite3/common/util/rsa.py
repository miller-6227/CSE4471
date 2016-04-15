
import random
import itertools
import fractions


class Crypto:

    # private variables as keys
    __n = 0
    __e = 0
    __d = 0

    def decrypt(self, cipher):
        message = ''
        for c in cipher:
            message += chr(pow(c, self.__d) % self.__n)
        return message

    def encrypt(self, message, e, n):
        cipher = []
        for c in message:
            cipher.append(pow(ord(c), e) % n) 
        return cipher 

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
        p = self.__get_primes(pow(2, bits))
        q = self.__get_primes(pow(2, bits))
        while (q==p):
            q = self.__get_primes(bits/2)

        # compute n = pq
        n = p * q
        phi = (p-1) * (q-1)

        # given a, n, and e, with 0 < a < n and e > 1, calculate a^e mod n
        while True:
            e = random.randint(3, phi - 1)
            if fractions.gcd(e, phi) == 1:
                break
        d = self.__multiplicative_inverse(e, phi)
        self.__n = n
        self.__e = e
        self.__d = d
        return (d, n)

    def __get_primes(self, bits):
        p = random.randint(3, bits-1) 
        while not self.__is_prime(p):
            if (p+2)>=(bits-1) or p%2==0:
                p = random.randint(3, bits-1)
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


'''
#### test
message = 'This is a test message'


crypto = Crypto()
crypto.generate_key(8)

print(message)
cipher = crypto.encrypt(message)
print(cipher)
dmessage = crypto.decrypt(cipher)
print(dmessage)


'''

