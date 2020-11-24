N = int(input())
ai = list(map(int,input().split()))
ai.sort(reverse = True)

ans = 0
for i in range(1,2*N,2):
    ans += ai[i]
print(ans)