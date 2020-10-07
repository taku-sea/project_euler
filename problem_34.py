import math
n = 2
answer = []
while n < 2540160:
    n += 1
    l = [math.factorial(int(i)) for i in list(str(n))]
    if n == sum(l):
        answer.append(n)

print(sum(answer))