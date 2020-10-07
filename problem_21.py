def d(n):
    l = [i for i in range(1, n) if n % i == 0]
    return sum(l)

answer = []
n = 0
while n < 10000:
    n += 1
    if n == d(d(n)) and n != d(n) and d(n) < 10000:
        answer.append(n)

print(sum(answer))