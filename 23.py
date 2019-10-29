from recs import primes

abundents = []
for i in range(12, 20162):
    if sum(primes.divisors(i)) > i:
        abundents.append(i)

sum_abundents = []
for i in range(len(abundents)):
    for j in range(i, len(abundents)):
        sum_abundents.append(abundents[i] + abundents[j])

s_abuns = list(set(sum_abundents))
non_abuns = []
for i in range(20162):
    if i not in s_abuns:
        non_abuns.append(i)
print(len(non_abuns))
print(sum(non_abuns))