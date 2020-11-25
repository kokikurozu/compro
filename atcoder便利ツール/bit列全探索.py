N = 3
for i in range(2**N):
    ls = [1]*N
    for j in range(len(ls)):
        if (i >> j) & 1:
            ls[j] = 0
    print(ls) #この位置にbit列が用意されるので、ここにコードを書く
#N個のビット列がすべてlsに格納される
#appendを利用する場合
N = 3
ls_list = []
for i in range(2**N):
    ls = [1]*N
    for j in range(len(ls)):
        if (i >> j) & 1:
            ls[j] = 0
    ls_list.append(ls)
print(ls_list)

'''
N=H
for i in range(2**N):
    ls = [1]*N
    for j in range(len(ls)):
        if (i >> j) & 1:
            ls[j] = 0
    Hbit.append(ls)
N=W
for i in range(2**N):
    la = [1]*N
    for j in range(len(la)):
        if (i >> j) & 1:
            la[j] = 0
    Wbit.append(la)
#print(Wbit)
#print(Hbit)
'''
#上記のような形で、bit列を二種類用意して使うこともある