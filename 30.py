def is_sum_5thpows(n):
    lnum = list(str(n))
    return n == sum([int(x) ** 5 for x in lnum])

fifth_pows = []
for n in range(2, 1000000):
    if is_sum_5thpows(n):
        fifth_pows.append(n)

print(len(fifth_pows))
print(sum(fifth_pows))