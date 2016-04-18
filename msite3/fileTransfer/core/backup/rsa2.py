
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
        return (e, n)

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
message = r'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00C\x00\x03\x02\x02\x03\x02\x02\x03\x03\x03\x03\x04\x03\x03\x04\x05\x08\x05\x05\x04\x04\x05\n\x07\x07\x06\x08\x0c\n\x0c\x0c\x0b\n\x0b\x0b\r\x0e\x12\x10\r\x0e\x11\x0e\x0b\x0b\x10\x16\x10\x11\x13\x14\x15\x15\x15\x0c\x0f\x17\x18\x16\x14\x18\x12\x14\x15\x14\xff\xdb\x00C\x01\x03\x04\x04\x05\x04\x05\t\x05\x05\t\x14\r\x0b\r\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\xff\xc0\x00\x11\x08\x048\x07\x80\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1d\x00\x00\x02\x03\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x04\x05\x06\x07\x08\x01\t\xff\xc4\x00Z\x10\x00\x01\x04\x01\x02\x04\x04\x03\x04\x07\x05\x05\x04\x06\x02\x13\x02\x00\x03\x04\x12\x05"2\x06\x13\x14B\x07#Rb\x15r\x82$3\x92\xa2\x01\x08\x16Ca\xb2\xc214S\xd2\xf0\x11%cs\xe2\x17!D\xf2\t&5T\x83\x93\xb36Adt\xa3\x187E\x84\xa4\xb4\xc3QU\xd3\'Fe\x91\xe3\xff\xc4\x00\x1c\x01\x01\x00\x03\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\xff\xc4\x00<\x11\x00\x02\x02\x01\x03\x02\x04\x03\x07\x03\x04\x03\x00\x02\x02\x03\x00\x01\x02\x11\x03\x12!1\x04A\x13"Qa\x05q\x812\x91\xa1\xb1\xc1\xd1\xf0\x14#\xe1\x063B\xf1\x15$4Rb%Cr\x92\xa2\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xfb\x0c\x01\x07\xe9E?\xee\xf6&\xa5\x0e\xab\xf4\xb3\xcf"H~\xa51\xa40V\x04I\x13\xa4?\x95\\\x08ih\xa5IE}@T\x9b\xfb\x93\x9a)\xeaV\x02\x18kJa\xa3Jd\x02\x01\x10`\x9e\x89\x10\n\x84\xd4J\xad`(\x92\x9a\x13\xa3z\x90\'zJ\x92\x99"\x01;\x10\t\xf5Y\x08\x04\xecKE-=H@D\x83L`){\xd4\xd8\x03\xd8 '

crypto = Crypto()
a,b = crypto.generate_key(8)

print(message)
cipher = crypto.encrypt(message, a,b)
print(cipher)
dmessage = crypto.decrypt(cipher)
print(dmessage)

'''
