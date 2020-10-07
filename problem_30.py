answer = []
l = []
for i in range(2, 354295):
    l = [int(x)**5 for x in list(str(i))]
    if i == sum(l):
        answer.append(i)
    l.clear()

print(sum(answer))