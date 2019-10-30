fib = [(0, 1), (1, 1), (2, 2)]

idx = 3
while len(str(fib[2][1])) < 1000:
    fib.append((idx, fib[1][1] + fib[2][1]))
    fib.pop(0)
    idx += 1

print(fib[2][0], len(str(fib[2][1])))