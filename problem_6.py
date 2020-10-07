sum_pow = sum([num**2 for num in range(1, 101)])
pow_sum = sum(range(1, 101)) ** 2
res = pow_sum - sum_pow
print(res)