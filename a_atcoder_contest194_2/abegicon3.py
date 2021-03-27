n,m = map(int,input().split())
xy=[map(int,input().split())for _ in range(m)]
start_max = 0
goal_min = 2000000
for i,j in xy:
    start_max = max(start_max,i)
    goal_min = min(goal_min,j)

if start_max <= goal_min:
    print(goal_min - start_max + 1)
else:
    print(0)