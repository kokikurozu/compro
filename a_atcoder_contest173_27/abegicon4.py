from collections import Counter

N = int(input())
Ai = list(map(int,input().split()))
Q = int(input())
ans = sum(Ai)
Ai_count = Counter(Ai)

for i in range(Q):
    bc = list(map(int,input().split()))
    ans += (bc[1] - bc[0]) * Ai_count[bc[0]]
    Ai_count[bc[1]] += Ai_count[bc[0]]
    Ai_count[bc[0]] = 0
    print(ans)