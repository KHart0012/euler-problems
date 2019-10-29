smallest_num = 0
nums = range(1, 21)
found = False
curr = 20
i = 0
num_true = 0
while not found:
    num_true = 0
    for i in nums:
        if curr % i == 0:
            num_true += 1
    if num_true == 20:
        found = True
        smallest_num = curr
    curr += 20

print(smallest_num)