coins = [0, 1, 2, 5, 10, 20, 50, 100, 200]
amt = 200

dyn_prog = [[0 for x in range(amt + 2)] for y in range(len(coins))]

for i in range(1, len(coins)):
    dyn_prog[i][1] = 1

for j in range(1, amt + 1):
    dyn_prog[1][j] = 1


for i in range(1, len(coins)):
    for j in range(2, amt + 2):
        dyn_prog[i][j] = dyn_prog[i - 1][j] + dyn_prog[i][j - coins[i]]

print(dyn_prog[len(coins) - 1][amt + 1])