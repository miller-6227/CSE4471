
import random





def decrypt(cipher, n, d):
    return modular.power(cipher, d, n)

def encrypt(message, n, e):
    return modular.power(message, e, n)

def extended_gcd(a, b):
    x, lastx, y, lasty, = 0, 1, 1, 0
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y
    return lastx, lasty


def generate_key(bits):

    # find two prime number, p and q
    p = get_primes(bits/2)
    q = get_primes(bits/2)
    while (q==p):
        q = get_primes(bits/2)

    # compute n = pq
    n = p * q
    phi = (p-1) * (q-1)

    # given a, n, and e, with 0 < a < n and e > 1, calculate a^e mod n
    while True:
        e = random.rand.int(3, phi - 1)
        if fractions.gcd(e, phi) == 1:
            break
    d = multiplicative_inverse(e, phi)
    return (n, e, d)


def get_primes(bits):
    get_random_t = lambda: random.getrandbits(bits) | 1 << bits | 1
    p = get_random_t()
    for i in itertools.count(1):
        if is_prime(p):
            return p
        else:
            if i % (bits * 2) == 0:
                p = get_random_t()
            else:
                p += 2

def is_prime(n):
    if n%2==0 or n%3==0:
        return True
    
    k = 6
    while (k-1) ** 2 <= n:
        if n % (k - 1) == 0 or n % (k + 1) == 0:
            return False
        k += 6
    return True

def multiplicative_inverse(e, n):
    x, y = extended_gcd(e, n)
    if x < 0:
        return n + x
    return x



#### test
n, e, d = generate_key(8)
print(n, e, d)
message = 123
print(message)
cipher = encrypt(message, n, e)
print(cipher)
dmessage = decrypt(cipher, n, d)
print(dmessage)




