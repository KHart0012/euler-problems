with open('texts/13.txt', 'r') as f:
    read_data = f.readlines()

nums = [int(x) for x in read_data]
print(sum(nums))