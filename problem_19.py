normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = 1900
pre = 1
answer = []
while year < 2000:
    year += 1
    if year % 4 != 0:
        for i in normal:
            if (i + pre) % 7 == 6:
                answer.append(1)
                pre = 6
            else:
                pre = (i + pre) % 7
    else:
        for i in leap:
            if (i + pre) % 7 == 6:
                answer.append(1)
                pre = 6
            else:
                pre = (i + pre) % 7

print(sum(answer))