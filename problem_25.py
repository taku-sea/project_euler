a = 1
b = 1
c = 0
n = 2
while c < 10 ** 999:
    n += 1
    c = a + b
    a = b
    b = c

print(n)