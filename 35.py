'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from recs import primes

def prime_rotations(n):
    rotations = [n]
    for i in range(len(str(n)) - 1):
        rotated_n = str(rotations[i])[1:] + str(rotations[i])[0]
        rotations.append(int(rotated_n))
    
    return rotations

MAX_NUM = 1000000

prs = primes.brute_force_prime_gen(MAX_NUM)
circular_primes = list()

bad_digits = [0, 2, 4, 5, 6, 8]

for p in prs:
    all_prime = True

    if all_prime:
        for d in list(str(p)):
            if int(d) in bad_digits:
                all_prime = False
    
    if all_prime:
        for r in prime_rotations(p):
            if not primes.is_prime(r):
                all_prime = False

    if all_prime:
        circular_primes.append(p)
        
    
print(len(sorted(circular_primes)))