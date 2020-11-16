N = int(input())
ab=[list(map(int,input().split()))for _ in range(N)]

ans = 0
for a,b in ab:
    ans += ((a+b)/2) * (b - a + 1)
print(int(ans))