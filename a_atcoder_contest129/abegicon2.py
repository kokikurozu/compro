n = int(input())
xy=[list(map(int,input().split()))for _ in range(n)]
ans = 0
for i in range(n-1):
    for j in range(i+1,n,1):
        if (xy[i][0] - xy[j][0]) != 0:
            tilt = (xy[i][1] - xy[j][1])/(xy[i][0] - xy[j][0])
        else:
            tilt = 2
        if -1 <= tilt <= 1:
            ans += 1
print(ans)