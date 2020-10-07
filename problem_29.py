answer = []
for a in range(2, 101):
    for b in range(2, 101):
        if not a**b in answer:
            answer.append(a**b)

print(len(answer))