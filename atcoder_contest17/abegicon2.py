N, K = map(int, input().split())
pi = list(map(int, input().split()))
pi.sort()
gokei = 0
for i in range(K):
    gokei += pi[i]
print(gokei)