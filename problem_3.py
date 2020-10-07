N = 600851475143
v = []
tmp = 1
while N > 1:
    tmp += 2
    if N%tmp == 0:
        v.append(tmp)
        while N%tmp == 0:
            N /= tmp

print(max(v))