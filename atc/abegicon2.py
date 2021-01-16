h,w = map(int,input().split())
y=[list(map(int,input().split()))for _ in range(h)]
min_now = 10000
for i in y:
    min_now = min(min_now,min(i))
ans = 0
for j in y:
    for k in j:
        ans += (k - min_now)
print(ans)