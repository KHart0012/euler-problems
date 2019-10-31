from recs import primes

def num_primes(a, b):
    n = 0
    while primes.is_prime((n ** 2) + (a * n) + b):
        n += 1
    return n

high_a = 0
high_b = 0
high_n = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        np = num_primes(a, b)
        if np > high_n:
            high_n = np
            high_a = a
            high_b = b

print(high_a * high_b)
