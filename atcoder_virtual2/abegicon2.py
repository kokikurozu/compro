import itertools

n,k = map(int,input().split())
ti = [list(map(int,input().split()))for _ in range(n)]
listn = [i+1 for i in range(n-1)]
all_keiro = list(itertools.permutations(listn, n-1))

ans = 0
for i in all_keiro:
    city_mae = 0
    city_ato = 0
    cnt = 0
    for j in i:
        city_mae = city_ato
        city_ato = j
        cnt += ti[city_mae][city_ato]
    cnt += ti[city_ato][0]
    if cnt == k:
        ans += 1
print(ans)