x = 0
while True:
    x += 1
    list_x = list(str(x))
    list_2x = list(str(2*x))
    list_3x = list(str(3*x))
    list_4x = list(str(4*x))
    list_5x = list(str(5*x))
    list_6x = list(str(6*x))
    if set(list_x) == set(list_2x) == set(list_3x) == set(list_4x) == set(list_5x) == set(list_6x):
        break

print(x)