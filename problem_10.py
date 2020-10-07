prime_list = [2]
n = 1
while n < 2 * (10**6):
    n += 2
    if all(n%p != 0 for p in prime_list):
        prime_list.append(n)

print(sum(prime_list))