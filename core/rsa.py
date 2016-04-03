# Implementation of RSA encryption



class PublicKey():


class PrivateKey():



def generate_key(length):
    # choose two distinct prime numbers p and q in a range(min, max)
    min_n = 
    max_n = 
    p, q = get_primes(min_n, max_n)    

    # compute n = pq
    # simplying Euler's totient function, compute phi = n - (p + q - 1)
    # choose an integer e s.t. e and phi are coprime
        # 1 < e < phi  AND gcd(e, phi) = 1
    # determine d as d === e^-1 (mod phi)
    
    # the public key is (n,e)
    # the private key is (d)

""" Return two prime numbers  """
def get_primes(length):



    return p, q
