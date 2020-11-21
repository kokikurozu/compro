N = int(input())
Ai = list(map(int,input().split()))
Bi = list(map(int,input().split()))

ans = 0
remaining = 0
for i in range(N):
    if Ai[i] - remaining >= 0:
        ans += remaining
    else:
        ans += Ai[i]
            if remaining >= 0:

    if  >= 0:
        ans += stock
        remaining = A[i] - stock
    else:
print(ans)