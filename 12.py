import math
from recs import primes

def gen_tri_num(n):
    return (n * (n + 1)) // 2

p_list = primes.prime_sieve(75000)

count = 10
while primes.num_divisors(gen_tri_num(count), p_list) < 500:
    count += 1

print(primes.num_divisors(gen_tri_num(count), p_list))
print(gen_tri_num(count))