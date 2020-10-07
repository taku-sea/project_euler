answer = []
n = 0
while n < 10**6:
    n += 1
    if str(n) == str(n)[::-1]:
        if format(n, 'b') == format(n, 'b')[::-1]:
            answer.append(n)

print(sum(answer))