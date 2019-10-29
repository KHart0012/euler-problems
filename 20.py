import math

factorial = list(str(math.factorial(100)))
digits = [int(x) for x in factorial]

print(sum(digits))