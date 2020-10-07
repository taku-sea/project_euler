n = "0"
for i in range(1, 1000001):
    n += str(i)

answer = int(n[1]) * int(n[10]) * int(n[100]) * int(n[1000]) * int(n[10000]) * int(n[100000]) * int(n[1000000])
print(answer)