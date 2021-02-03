N = int(input())
Ai = list(map(int,input().split()))
Ai.sort(reverse = True)
ans = 0
for i in range(N):
    ans += (Ai[i] * (N - 2 * i - 1))
print(ans)