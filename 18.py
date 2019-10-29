def rz(string):
    if string.startswith('0'):
        return int(string[1:])
    return int(string)

with open('texts/18.txt', 'r') as f:
    read_data = f.readlines()

split_list = [x.split() for x in read_data]

for i in range(len(split_list)):
    for j in range(len(split_list[i])):
        split_list[i][j] = rz(split_list[i][j])


for i in range(len(split_list) - 1):
    #print(split_list[:i + 1])
    #print()
    for j in range(len(split_list[i + 1])):
        # if we are at the start of the list, node only has one parent
        if j - 1 < 0:
            split_list[i + 1][j] += split_list[i][j]
       
        # if we are at the end of the list, node also only has one parent
        elif j >= len(split_list[i]):
            split_list[i + 1][j] += split_list[i][j-1]
        
        # Nodes in the middle have 2 parents to choose from
        else:
            split_list[i + 1][j] = max(split_list[i][j-1] + split_list[i + 1][j], split_list[i][j] + split_list[i + 1][j])
      

print(max(split_list[len(split_list) - 1]))