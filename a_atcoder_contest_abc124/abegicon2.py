n = int(input())
hi = list(map(int,input().split()))
ans = 0
height = 0
for i in range(n):
    if hi[i] >= height:
        ans += 1
    height = max(hi[i],height)
print(ans)