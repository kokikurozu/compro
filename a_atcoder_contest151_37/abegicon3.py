N,M = map(int,input().split())
ps=[list(map(str,input().split()))for _ in range(M)]
toi = [0 for _ in range(N)]
cnt_WA = 0
cnt_AC = 0
for p,s in ps:
    if s == 'WA':
        toi[int(p)-1] += 1
    else:
        if toi[int(p)-1] >= 0:
            cnt_WA += toi[int(p)-1]
            cnt_AC += 1
            toi[int(p)-1] = -2 * 10 ** 5
print(cnt_AC, cnt_WA)