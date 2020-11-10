N = int(input())
Ai = list(map(int,input().split()))
now_sum = 0
now_max = 0
now_point = 0
max_Ai = -1

for i in range(N):
    now_sum += Ai[i]
    now_point += now_sum
    if now_max < now_point:
        now_max = now_point
        max_Ai = [i]
    elif now_max == now_point:
        max_Ai.append(i)

now_point_foward = now_max
now_point_back = now_max
for i in range(max_Ai + 1):
    now_point_foward += Ai[i]
    now_max = max(now_max,now_point_foward)
for i in range(max_Ai, -1, -1):
    now_point_back += Ai[i]
    now_max = max(now_max,now_point_back)

if now_max <= 0:
    print(0)
else:
    print(now_max)