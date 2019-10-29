num_dict = {
    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety'
}

def num_builder(num):
    length = len(str(num))
    if length == 1:
        return num_dict[num]
    elif length == 2:
        if num < 20:
            return num_dict[num]
        return num_dict[(num + (10 - (num % 10))) - 10] + num_dict[num % 10]
    elif length == 3:
        if int(str(num)[1]) * 10 == 10:
            return num_dict[int(str(num)[0])] + 'hundredand' + num_dict[num - (int(str(num)[0]) * 100)]
        elif num % 100 == 0:
            return num_dict[int(str(num)[0])] + 'hundred'
        return num_dict[int(str(num)[0])] + 'hundredand' + num_dict[int(str(num)[1]) * 10] + num_dict[num % 10]
    else:
        return "onethousand"

numbers = []
for i in range(1, 1001):
    numbers.append(num_builder(i))

total_length = 0
for num in numbers:
    total_length += len(num)

print(total_length)