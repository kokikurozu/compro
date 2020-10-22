N,K,M = map(int,input().split())
Ai = list(map(int,input().split()))

if N * M > sum(Ai) + K:
    print(-1)
elif (N * M - sum(Ai)) < 0:
    print(0)
else:
    print((N * M - sum(Ai)))
