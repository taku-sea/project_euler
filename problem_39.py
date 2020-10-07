answer = {}
l = []
p = 0
n = 0
while p < 1000:
    p += 1
    for a in range(1, p):
        for b in range(a, p):
            if (p - a - b) == ((a**2 + b**2)**0.5):
                l.append(n)
    answer[len(l)] = p
    l.clear()

print(answer[max(list(answer.keys()))])