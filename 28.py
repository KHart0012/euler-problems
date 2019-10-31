size = 1001
grid = [[0 for y in range(size)] for x in range(size)]

n = 1

start = size // 2
x = start
y = start
direct = 'up'
right = 1
down = 1
left = 2
up = 0
while n <= size ** 2:
    if direct == 'right':
        for i in range(right):
            grid[y][x] = n
            n += 1
            x += 1
        direct = 'down'
        right += 2
    elif direct == 'down':
        for i in range(down):
            grid[y][x] = n
            n += 1
            y += 1
        direct = 'left'
        down += 2
    elif direct == 'left':
        for i in range(left):
            grid[y][x] = n
            n += 1
            x -= 1
        direct = 'up'
        left += 2
    elif direct == 'up':
        for i in range(up):
            grid[y][x] = n
            n += 1
            y -= 1
        direct = 'right'
        up += 2
    
        
s = 0

i = 0
for l in grid[:size // 2]:
    s += (l[i] + l[(size - 1) - i])
    i += 1

for l in grid[size // 2:]:
    s += (l[i] + l[(size - 1) - i])
    i += 1

print(s - 1)