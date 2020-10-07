prime_list = [2]
n = 1
while len(prime_list) < 10001:
    n += 2
    if all(n%p != 0 for p in prime_list):
        prime_list.append(n)

print(max(prime_list))