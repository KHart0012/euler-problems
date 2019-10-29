import math

def prime_sieve(n):
    # Generate the sieve
    primes = [False, False]
    for i in range(n - 1):
        primes.append(True)
    for i in range(2, round(math.sqrt(n))):
        if primes[i]:
            multi = 1
            for j in range(i ** 2, n + 1, multi * i):
                primes[j] = False
                multi += 1
    
    # Grab the actual prime numbers out of it
    prime_nums = []
    for i in range(len(primes)):
        if primes[i]:
            prime_nums.append(i)
    
    return prime_nums

def prime_factors(n):
    list_primes = prime_sieve(n)
    prime_factors = []
    for prime in list_primes:
        if n % prime == 0:
            prime_factors.append(prime)
    return prime_factors

def prime_factorization(n):
    factors = []
    primes = prime_factors(n)
    new_n = n
    pcount = 0
    while not is_prime(new_n):
        if new_n % primes[pcount] == 0:
            new_n = new_n // primes[pcount]
            factors.append([primes[pcount], new_n])
            pcount = 0
        else:
            pcount += 1
        
    
    pfactors = []
    for f in factors:
        pfactors.append(f[0])
        if is_prime(f[1]):
            pfactors.append(f[1])

    return pfactors

def num_divisors(n, prime_list):
    factors = []
    primes = prime_list
    new_n = n
    pcount = 0
    while not is_prime(new_n):
        if new_n % primes[pcount] == 0:
            new_n = new_n // primes[pcount]
            factors.append([primes[pcount], new_n])
            pcount = 0
        else:
            pcount += 1
        
    
    pfactors = []
    for f in factors:
        pfactors.append(f[0])
        if is_prime(f[1]):
            pfactors.append(f[1])


    count_primes = [(p, pfactors.count(p)) for p in primes if pfactors.count(p) > 0]
    prod = 1
    for pfs in count_primes:
        prod *= (pfs[1] + 1)
    return prod

def divisors(n):
    divs = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divs.append(i)
    return divs

def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nth_prime(n):
    if n == 1:
        return 2
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1

#print(num_divisors(228))