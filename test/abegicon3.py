n,m = map(int,input().split())
ab=[map(int,input().split())for _ in range(m)]
k = int(input())
cd=[map(int,input().split())for _ in range(k)]
sara = [0 for i in range(n)]
ans = 0
ans_max = 0
#bit列
N = k
ls_list = []
for i in range(2**N):
    ls = [1]*N
    for j in range(len(ls)):
        if (i >> j) & 1:
            ls[j] = 0
    ls_list.append(ls)
for i in ls_list:
    for j in range(k):
        y = list(cd[j])
        sara[y[i[j]]-1] += 1
    for l in ab:
        x = list(l)
        #print(sara[x[0]-1])
        #print(sara[x[1]-1])
        if sara[x[0]-1] >= 1 and sara[x[1]-1] >=1:
            ans += 1
    sara = [0 for i in range(n)]
    ans_max = max(ans_max,ans)
    ans = 0
print(ans)