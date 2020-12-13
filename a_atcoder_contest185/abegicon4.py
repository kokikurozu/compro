import math

n,m = map(int,input().split())
ai = list(map(int,input().split()))
cnt = 0
ai.sort()
min_k = 10**10
if m != 0:
    if ai[0] - 1 != 0:
        min_k = ai[0]-1

    for j in range(m-1):
        if ai[j+1] - ai[j] - 1 != 0:
            min_k = min(min_k,ai[j+1] - ai[j] - 1)

    cnt += math.ceil((ai[0] - 1) / min_k)

    for i in range(m-1):
        cnt += math.ceil((ai[i+1] - ai[i] - 1) / min_k)

    cnt += math.ceil((n - ai[m-1]) / min_k)

    print(cnt)
else:
    print(1)