'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

import math

def digits(num):
    return [int(d) for d in str(num)]

def factorial_digit_sum(digits):
    return sum(math.factorial(d) for d in digits)


factorials = [math.factorial(d) for d in digits('0123456789')]
#print(factorials)

MAX_NUM = 10000000
current = 10
valid = []

while current < MAX_NUM:
    dis = digits(current)
    total = sum(factorials[d] for d in dis)
    if total == current:
        valid.append(current)
    
    if current < total:
        current += 1
    else:
        current += 5

print(valid)