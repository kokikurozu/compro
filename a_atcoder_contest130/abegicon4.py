import bisect

n, k = map(int,input().split())
ai = list(map(int,input().split()))
s = [0] * (n+1)

for i in range(n):
    s[i+1] = s[i] + ai[i]

ans = 0
for i in range(n):
    x = k + s[i]
    ans += (n + 1 - bisect.bisect_left(s,x))
print(ans)