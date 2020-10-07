T = [(i*(i+1))//2 for i in range(1, 10**5)]
P = [(i*(3*i-1))//2 for i in range(1, 10**5)]
H = [i*(2*i-1) for i in range(1, 10**5)]
answer = [i for i in T if i in P and i in H]

#出力から40755の次に大きい数字が答え。
#C++のupper_boundみたいなことができればいいんですが、実装が面倒なので…
print(answer)