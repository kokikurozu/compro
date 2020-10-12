H, W, K = map(int,input().split())
xy=[list(map(str,list(input())))for _ in range(H)]

Hbit=[]
Wbit=[]
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
ans = 0

for j in Wbit:
    for k in Hbit:
        count = 0
        for l in range(H):
            for m in range(W):
                if j[m] == 0 and k[l] == 0 and  xy[l][m] == '#':
                    count += 1
        if count == K:
            ans += 1
print(ans)