n,q = map(int,input().split())
ai = list(map(int,input().split()))
ai_hako = [0 for i in range(n)]
ai_hako[0] = ai[0]
use_new_hako = [0 for i in range(n)]
for j in range(n-1):
    ai_hako[j+1] = ai_hako[j] ^ ai_hako[j+1]

ai_new_hako = [0 for i in range(n)]
cnt = 0
now_cnt = 0

for i in range(q):
    t,x,y = map(int,input().split())
    if t == 1:
        ai[x-1] = ai[x-1] ^ y
    else:
        if x == 1:
            ai_new_hako[cnt] = ai[x-1] ^ y
            cnt += 1
            now_cnt = 0
        else:
            ans = ai_hako[y-1] ^ ai_hako[x-2]