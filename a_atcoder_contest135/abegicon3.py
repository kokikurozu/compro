N = int(input())
Ai = list(map(int,input().split()))
Bi = list(map(int,input().split()))

ans = 0
stock = 0
for i in range(N):
    if Ai[i] - stock >= 0:
        ans += Ai[i] - stock
print(ans)