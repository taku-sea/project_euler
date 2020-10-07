a, b, c = 1, 2, 0
answer = 2
while c <= 4 * (10**6):
    c = a+b
    a = b
    b = c
    if c%2 == 0:
        answer += c

print(answer)