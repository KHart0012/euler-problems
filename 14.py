def collatz(n):
    if n % 2 == 0:
        return n // 2
    return (3 * n) + 1

def collatz_chain(n):
    collatz_count = 0
    new_n = n
    while collatz(new_n) != 1:
        new_n = collatz(new_n)
        collatz_count += 1 
    return collatz_count

longest_sequence = 0
longest_sequence_num = 0

for i in range(2, 1000001):
    curr = collatz_chain(i)
    if curr > longest_sequence:
        longest_sequence = curr
        longest_sequence_num = i

print(longest_sequence_num)
print(longest_sequence)