N, K = map(int, input().split())
Ni = [0 for i in range(N)]
for j in range(K):
    di = int(input())
    Ai = list(map(int, input().split()))
    for x in Ai:
        Ni[x - 1] = 1

print(Ni.count(0))

