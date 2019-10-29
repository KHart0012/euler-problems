import math
from recs import primes

num = 600851475143
prime_factors = primes.prime_factorization(num)

print(prime_factors[len(prime_factors) - 1])