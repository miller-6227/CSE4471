# Implementation of RSA encryption

import random
import array
import math


def decrypt(private_key, text):

    # separate the private key into its two parts
    key, n = private_key

    # decrypt using the key
    d_text = [chr((char ** key) % n) for char in text]
    
    return ''.join(d_text)

def encrypt(public_key, text):
    
    # separate the public key into its two parts
    key, n = public_key

    # encrypt the text
    e_text = [((ord(char) ** key) % key) % n for char in text]

    return e_text


""" follow the general steps to generate a private and public key """
def generate_key(length):
   
     # (1) choose two distinct prime numbers p and q in a range(min, max)
    min_n = pow(2, length-1)
    max_n = pow(2, length) -1
    # get a list of all primes in the range
    primes = [ i for i in range(min_n, max_n) if is_prime(i)]

    # randomly select two of the values in that array
    if len(primes) >= 2:
        p = random.choice(primes)
        primes.remove(p)
        q = random.choice(primes)                
    else:
        # error
        print("Error choosing primes")
        quit()

    # (2) compute n = pq
    n = p * q

    # (3) simplying Euler's totient function, compute phi = n - (p + q - 1)
    phi = (p-1) * (q-1)

    # (4) choose an integer e s.t. e and phi are coprime
        # 1 < e < phi  AND gcd(e, phi) = 1
    for e in range(3, phi, 2):
        if is_coprime(e, phi):
            break
    else:
        # no co prime
        print("error with coprimes")
        quit()

    print("5", phi)

    # (5) determine d as d === e^-1 (mod phi)
    d = multiplicative_inverse(e, phi)

    print("done", d)

    # the public key is (e,n)
    # the private key is (d,n)
    return ((e,n),(d,n))

""" Return two prime numbers in a given range"""
def get_primes(minv, maxv):
    
    # check if it's possible first
    if minv >= maxv:
        return []

    print(minv, maxv)

    # initalize empty prime array
    primes = [2]

    for n in range(minv, maxv+1):
        # collect the prime numbers
        for p in primes:
            # check if the number is prime
            if n % p == 0:
                break
        else:
            primes.append(n)
    
    # remove prime numbers less than the min value
    while primes and primes[0] < minv:
        del primes[0]

    return primes


""" determine if a and b are coprime """
def is_coprime(a, b):
    for n in range(2, min(a,b)+1):
        if a % n == b % n == 0:
            return False
    return True

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 -w 
    return True


def multiplicative_inverse(e, phi):
    a, b = e, phi
    x, lastx, y, lasty = 0, 1, 1, 0
    while b != 0:
        q, r = divmod(a,b)
        a, b = b, r
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y
    if lastx < 0:
        return phi + lastx
    return lastx


## test

text = "This is a test message"
print("Original: ", text)

privatekey, publickey = generate_key(len(text))

print("private: ", privatekey)
print("public: ", publickey)

etext = encrypt(publickey, text)
print("Encrypted: ", etext)

dtext = decrypt(privatekey, etext)
print("Decypted: ", dtext)



