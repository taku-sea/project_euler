answer = []
for a in range(0, 201):
    for b in range(0, 101):
        for c in range(0, 41):
            for d in range(0, 21):
                for e in range(0, 11):
                    for f in range(0, 5):
                        for g in range(0, 3):
                            for h in range(0, 2):
                                if (a + 2*b + c*5 + d*10 + e*20 + f*50 + g*100 + h*200) == 200:
                                    answer.append(0)

print(len(answer))