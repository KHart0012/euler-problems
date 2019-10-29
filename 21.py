from recs import primes

sums = [0]
amicable_nums = [False]
for i in range(1, 10000):
    sums.append(sum(primes.divisors(i)))
    amicable_nums.append(False)

'''
a = sums[220]
b = sums[a]

print(a, b, b == 220)
'''

for i in range(1, len(sums)):
    if sums[i] < 10000 and sums[sums[i]] < 10000:
        a = sums[i]
        b = sums[a]
        if a != b and b == i:
            amicable_nums[i] = True
            amicable_nums[a] = True


am_nums = []
for i in range(1, len(amicable_nums)):
    if amicable_nums[i]:
        am_nums.append(i)

print(am_nums)
print(sum(am_nums))