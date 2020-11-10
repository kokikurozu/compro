N = int(input())
Hi = list(map(int,input().split()))

cnt = 0
now_heihgt = Hi[0]
now_max = 0
for i in range(1, N):
    if now_heihgt >= Hi[i]:
        cnt += 1
    else:
        now_max = max(now_max,cnt)
        cnt = 0
    now_heihgt = Hi[i]
now_max = max(now_max,cnt)

print(now_max)