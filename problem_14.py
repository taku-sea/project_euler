answer = []
l = []
n = 1
num = 1
while n < 10**6:
    if num == 1:
        l.append(num)
        answer.append(len(l))
        l.clear()
        n += 1
        num = n
    elif num % 2 == 0:
        l.append(num)
        num = num / 2
    else:
        l.append(num)
        num = 3*num + 1

print(answer.index(max(answer)) + 1)