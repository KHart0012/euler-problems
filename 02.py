fibs = [1, 2]
prev = 0
curr = 1
num3 = 0
total = 2
while num3 < 4000000:
    num3 = fibs[prev] + fibs[curr]
    fibs.append(num3)
    prev += 1
    curr += 1
    if num3 % 2 == 0:
        total += num3

print(total)
