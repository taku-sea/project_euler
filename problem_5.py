res = 0
while True:
    res += 1
    flag = 1
    for n in range(1, 21):
        if res%n:
            flag = 0
    if flag:
        print(res)
        break