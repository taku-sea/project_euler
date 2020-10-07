n = 0
l = []
abundant = []
while n < 28123:
    n += 1
    for i in range(1, ((n+1)//2)+1):
        if  n % i == 0:
            l.append(i)
    if sum(l) > n:
        abundant.append(n)
    l.clear()

n = 0
answer = []
while n < 28123:
    n += 1
    if not any((n - i) in abundant for i in abundant):
        answer.append(n)

print(sum(answer))