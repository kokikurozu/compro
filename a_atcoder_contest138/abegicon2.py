N = int(input())
Ai = list(map(int,input().split()))
ans = 0
for i in Ai:
    ans += 1/i

print(1/ans)