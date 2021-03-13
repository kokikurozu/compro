import copy
n,m,q = map(int,input().split())
wv=[list(map(int,input().split()))for _ in range(n)]
xi = list(map(int,input().split()))
#wv=[list(map(int,input().split()))for _ in range(n)]
switch_wv = []
for k in range(n):
    switch_wv.append([wv[k][1],wv[k][0]])
switch_wv.sort(reverse=True)
#print(switch_wv)

for i in range(q):
    ans = 0
    l,r = map(int,input().split())
    now_xi = copy.deepcopy(xi)
    for j in range(l-1,r,1):
        now_xi[j] = 0
    now_xi = sorted(now_xi,reverse=True)
    for o,p in switch_wv:    
        for i in range(m-1):
            if now_xi[i] >= p >= now_xi[i+1]:
                now_xi[i] = 0
                ans += o
    print(ans)