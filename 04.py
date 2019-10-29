def reverse(string):
    return string[len(string)::-1]

def is_palimdrome(num):
    if str(num)[0:3] == reverse(str(num)[3:]):
        return True
    return False

highest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        num = i * j
        if is_palimdrome(num):
            if num > highest:
                highest = num

print(highest)