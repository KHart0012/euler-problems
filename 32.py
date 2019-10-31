from itertools import permutations

perms = permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

def is_pandigital(ma, mul, prod):
    if ma * mul == prod:
        return True
    return False

   
pans = set()
prods = []
perm_is_pan = False
for p in perms:
    for i in range(3):
        ma = int(''.join(list(p[:i + 1])))
        if ma != 1:
            mul = int(''.join(list(p[i + 1:(i + 5) - i])))
            prod = int(''.join(list(p[(i + 5) - i:])))
            if is_pandigital(ma, mul, prod):
                pans.add(prod)
            prods.append((ma, mul, prod))

print((39, 186, 7254) in prods or (186, 39, 7254) in prods)
print(prods[1000:1050])
print(is_pandigital(186, 39, 7254))
print(sum(list(pans)))