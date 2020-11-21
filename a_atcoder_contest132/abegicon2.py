n = int(input())
pi = list(map(int,input().split()))
#練習
listpi = [0 for _ in range(3)]
listpi[0] = pi[0]
listpi[1] = pi[1]
ans = 0
for i in range(n-2):
    listpi[(i+2) % 3] = pi[i+2]
    S = sorted(listpi)
    if pi[i+1] == S[1]:
        ans += 1

print(ans)