mod = 2019
l,r = map(int,input().split())
ans = 2019
if r-l >=2019:
    ans = 0
else:
    for i in range(l,r,1):
        for j in range(i+1,r+1,1):
            x = ((i % mod) * (j % mod)) % mod
            ans = min(ans,x)
print(ans)