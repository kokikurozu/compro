n,x = map(int,input().split())
xy=[list(map(int,input().split()))for _ in range(n)]
alc = 0
ans = 0
for i in range(n):
    ans += 1
    alc += (xy[i][0] * xy [i][1] / 100)
    if alc > x:
        break
if alc <= x:
    ans = -1

print(ans)