def name_value(name):
    values = [ord(x) - 64 for x in list(name)]
    return sum(values)

with open('texts/22.txt', 'r') as f:
    read_data = f.readline()


name_list = str(read_data).split(",")
names = list(sorted([x.strip('\"') for x in name_list]))
name_values = [name_value(x) * (names.index(x) + 1) for x in names]
print(sum(name_values))