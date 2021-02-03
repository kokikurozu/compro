n,x = map(int,input().split())
xy=[list(map(int,input().split()))for _ in range(n)]
cnt = 0
alc = 0
x = x * 100
for i,j in xy:
    cnt += 1
    alc += i*j
    if alc > x:
        break

if alc <= x:
    cnt = -1

print(cnt)