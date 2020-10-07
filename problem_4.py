v = []
for a in range(100, 1000):
    for b in range(100, 1000):
        n = a*b
        if str(n) == str(n)[::-1]:
            v.append(n)

print(max(v))