'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

def is_nontrivial(num, den):
    # Get rid of trivial solutions
    if ('0' in str(num) or '0' in str(den)):
        return False

    if (str(num)[1] in str(den)[1]):
        return False

    no_num1 = num // 10
    no_den0 = den % 10
    
    if (num / den == no_num1 / no_den0):
        return True
    
    return False


def shares_digits(num, den):
    if (str(num)[0] not in str(den) and str(num)[1] not in str(den)):
        return False
    return True


numerator = 11
denominator = 12

nontrivial = []

while len(nontrivial) < 4 and numerator < 100 and denominator < 100:
    while numerator < denominator:
        if shares_digits(numerator, denominator):
            if is_nontrivial(numerator, denominator):
                nontrivial.append((numerator, denominator))
        numerator += 1
    numerator = 11
    denominator += 1

print(nontrivial)