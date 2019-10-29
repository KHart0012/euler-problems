prev = []
curr = [2, 1]

for i in range(19):
    prev = curr.copy()
    prev.append(0)

    curr.insert(0, 2 * sum(prev))
    for j in range(1, len(curr) - 1):
        curr[j] = sum(prev[j - 1:])
    

print(curr)