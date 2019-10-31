from decimal import *

getcontext().prec = 2000

deci = []
for i in range(100, 1000):
    deci.append((str(Decimal(1) / Decimal(i)), i))


longest_match = 0
pattern = ''
longest_match_len = 0
for d in deci:
    #print(d)
    if len(d[0]) > 10:
        start = 2
        stop = 4
        for i in range(len(d[0])):
            if stop + (stop - start) < len(d[0]): # make sure we don't hit index out of bounds
                if d[0][start:stop] == d[0][start + (stop - start):stop + (stop - start)]: # check if patterns match
                    if stop - start > longest_match_len and d[0][start] * 50 != d[0][start:start + 50]:
                        longest_match_len = stop - start
                        longest_match = d[1]
                        pattern = d[0][start:stop] + ' ' + d[0][stop:stop + (stop - start)]
                    i = len(d[0])
                else:
                    stop += 1
                    if start + 1 != stop:  
                        if d[0][start + 1:stop] == d[0][start + (stop - start):stop + (stop - start)]:
                            start += 1

print(longest_match)
#print(Decimal(1) / Decimal(longest_match))
print(pattern)
print(longest_match_len)    