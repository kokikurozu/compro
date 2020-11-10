N = int(input())
Ai = list(map(int,input().split()))
now_sum = 0
now_max = -200000000
now_point = 0
max_Ai = []

for i in range(N):
    now_sum += Ai[i]
    now_point += now_sum
    if now_max < now_point:
        now_max = now_point
        max_Ai = [i]
    elif now_max == now_point:
        max_Ai.append(i)

save = now_max

for x in max_Ai:
    now_point_foward = save
    now_point_back = save
    if (x + 1) != N:
        for i in range(x+1):
            now_point_foward += Ai[i]
            now_max = max(now_max,now_point_foward)
    for i in range(x, -1, -1):
        now_point_back -= Ai[i]
        now_max = max(now_max,now_point_back)

if now_max <= 0:
    print(0)
else:
    print(now_max)