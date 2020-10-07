sum_mul_3 = sum([number for number in range(1, 1000) if number%3 == 0])
sum_mul_5 = sum([number for number in range(1, 1000) if number%5 == 0])
sum_mul_15 = sum([number for number in range(1, 1000) if number%15 == 0])
answer = sum_mul_3 + sum_mul_5 - sum_mul_15
print(answer)