N, K = map(int,input().split())
A = list(map(int, input().split()))
A.insert(0, 0)
root = [0 for i in range(N + 1)]
root[1] = 1
now = A[1]
loop = 0
getloop = 0
startloop = -1
mae_now = -1
for j in range(K):
    root[now] += 1
    if root[now] == 3:
        startloop = now
        break
    if root[now] == 2:
        loop += 1
    if root[now] == 1:
        getloop += 1
    mae_now = now
    now = A[now]
if startloop == -1:
    print(mae_now)
if startloop != -1:
    nokoriloop = K % loop + getloop
    now = startloop
    for i in range(nokoriloop):
        now = A[now]
    print(now)