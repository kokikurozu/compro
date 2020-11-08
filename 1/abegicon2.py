N = int(input())
Ai = list(map(int,input().split()))
now_max = 0
now_k = 0
for i in range(2, 101, 1):
    cnt = 0
    for j in Ai:
        if j == (j//i * i):
            cnt += 1
    if now_max != max(now_max,cnt):
        now_max = max(now_max,cnt)
        now_k = i

print(now_k)