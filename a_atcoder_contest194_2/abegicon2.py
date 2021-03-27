n = int(input())

xy = [list(map(int,input().split())) for _ in range(n)]

task = 10000000
for i in range(n):
    for j in range(n):
        if i == j:
            task = min(task, xy[i][0] + xy[j][1])
        else:
            task = min(task,max(xy[i][0], xy[j][1]))

print(task)