N = 3
for i in range(2**N):
    ls = [1]*N
    for j in range(len(ls)):
        if (i >> j) & 1:
            ls[j] = 0
    print(ls)
#N個のビット列がすべてlsに格納される