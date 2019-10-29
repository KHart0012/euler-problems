sum_squares = range(1, 101)
sum_sq = 0
for i in sum_squares:
    sum_sq += i ** 2

square_sum = range(1, 101)
sq_sum = sum(square_sum) ** 2

print(sq_sum - sum_sq)