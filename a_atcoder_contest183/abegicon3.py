import itertools

N,K = map(int,input().split())
xy=[list(map(int,input().split()))for _ in range(N)]
ans = 0
listN = [i+1 for i in range(N-1)]
all_list = list(itertools.permutations(listN, N-1))

for list_i in all_list:
    cnt = 0
    pre_city = 0
    now_city = 0
    for i in list_i:
        pre_city = now_city
        now_city = i
        cnt += xy[pre_city][now_city]
    cnt += xy[now_city][0]
    if cnt == K:
        ans += 1

print(ans)