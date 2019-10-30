from itertools import permutations

perms = permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
#perms = permutations(['0', '1', '2'])

str_perms = []

for i in list(perms):
    str_perms.append(''.join(list(list(i))))

print(sorted(str_perms)[999999:1000002])